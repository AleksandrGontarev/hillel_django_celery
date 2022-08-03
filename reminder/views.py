from datetime import datetime, timedelta

from django.shortcuts import render


from .forms import ReminderForm
from .tasks import send_email


def home(request):
    return render(request, "reminder/home.html")


def reminder(request):

    if "submit" in request.GET:
        reminder_form = ReminderForm(request.GET)
        if reminder_form.is_valid():
            email = reminder_form.cleaned_data["email"]
            text_reminder = reminder_form.cleaned_data["text_reminder"]
            data_reminder = reminder_form.cleaned_data["data_reminder"]

            data_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data_user = data_reminder.strftime("%Y-%m-%d %H:%M:%S")
            data_delta = (datetime.now() + timedelta(days=2)).strftime("%Y-%m-%d %H:%M:%S")
            if (data_user > data_now) and (data_user <= data_delta):
                send_email.s(email, text_reminder, data_reminder).apply_async(eta=data_reminder)
            else:
                errors = f"ERROR Data must be between {data_now} an {data_delta}"
                return render(
                    request,
                    "reminder/reminder.html",
                    {"reminder_form": reminder_form, "errors": errors, }
                )

    else:
        reminder_form = ReminderForm()
    return render(
        request,
        "reminder/reminder.html",
        {"reminder_form": reminder_form, }
    )
