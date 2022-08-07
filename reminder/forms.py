from django.utils import timezone
from datetime import datetime, timedelta
from django import forms
from django.core.exceptions import ValidationError


class ReminderForm(forms.Form):

    email = forms.EmailField(max_length=100, required=True)
    text_reminder = forms.CharField(max_length=254, required=True)
    data_reminder = forms.DateTimeField(label='Data',
                                        initial=datetime.now(),
                                        required=True,
                                        help_text='date fill template 2022-08-05 17:58:48'
                                        )

    def clean_data_reminder(self):
        data_reminder = self.cleaned_data['data_reminder']
        data_now = timezone.now()
        data_user = data_reminder
        data_delta = data_now + timedelta(days=2)
        if (data_user > data_now) and (data_user <= data_delta):
            return data_reminder
        else:
            raise ValidationError(f"Error Data must be between {data_now + timedelta(hours=3)}"
                                  f" an {data_delta + timedelta(hours=3)}")
