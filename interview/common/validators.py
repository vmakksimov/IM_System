from django.core.exceptions import ValidationError


def only_letters_validator(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Value must contain only letters')


def validate_if_number_starts_with_country_code(value):
    country_code = value[0]
    number = value[1:]
    if country_code == '0':
        raise ValidationError('You number must start with your country code in front.')
    for char in number:
        if not char.isdigit():
            raise ValidationError('You must input only digits.')