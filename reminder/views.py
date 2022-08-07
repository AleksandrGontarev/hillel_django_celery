from datetime import timedelta, datetime
from django.utils import timezone
from django.shortcuts import render


from .forms import ReminderForm
from .tasks import send


def home(request):
    return render(request, "reminder/home.html")


def reminder(request):

    if request.method == "POST":
        reminder_form = ReminderForm(request.POST)
        if reminder_form.is_valid():
            email = reminder_form.cleaned_data["email"]
            text_reminder = reminder_form.cleaned_data["text_reminder"]
            data_reminder = reminder_form.cleaned_data["data_reminder"]
            send.s(email, text_reminder).apply_async(eta=data_reminder)
            return render(
                request,
                "reminder/reminder.html",
                {"reminder_form": reminder_form}
            )

    else:
        reminder_form = ReminderForm()
    return render(
        request,
        "reminder/reminder.html",
        {"reminder_form": reminder_form, }
    )
