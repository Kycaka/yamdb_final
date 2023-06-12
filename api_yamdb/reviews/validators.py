from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_year(value):
    """Проверка года на будущее время."""
    if value > timezone.now().year:
        raise ValidationError(
            'Марти, ты опять взял Делориан без спроса?!',
        )
    return value
