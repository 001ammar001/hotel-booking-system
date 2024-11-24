from django.core.exceptions import ValidationError
from django.utils.timezone import datetime, timedelta


def start_date_validator(date):
    now = datetime.now().date()
    if date < (now + timedelta(days=1)):
        raise ValidationError(f'you must enter a date in the present')
