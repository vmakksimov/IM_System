from django.core.validators import MinLengthValidator
from django.db import models

from .common.validators import validate_if_number_starts_with_country_code, \
    only_letters_validator


# Create your models here.
class Interview(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    LAST_NAME_MIN_LENGTH = 2
    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'
    PENDING = 'Pending'
    APPROVED = 'Approved'
    REJECTED = 'Rejected'
    STATUS = [(x, x) for x in (PENDING, APPROVED, REJECTED, DO_NOT_SHOW)]
    GENDERS = [(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]

    candidate_first_name = models.CharField(max_length=10,
                                            validators=(
                                                only_letters_validator, MinLengthValidator(FIRST_NAME_MIN_LENGTH)),
                                            null=False,
                                            blank=False,
                                            default=None,
                                            )
    candidate_last_name = models.CharField(max_length=10,
                                           validators=(
                                               only_letters_validator, MinLengthValidator(LAST_NAME_MIN_LENGTH)),
                                           null=False,
                                           blank=False,
                                           default=None
                                           )

    date_for_interview = models.DateField(
        null=True,
        blank=True,

    )

    email = models.EmailField(
        null=True,
        blank=True,
    )

    mobile_number = models.CharField(
        max_length=13,
        validators=(
            validate_if_number_starts_with_country_code,
            MinLengthValidator(10, message='The number is incorrect.')
        )
    )

    gender = models.CharField(
        max_length=max(len(x) for x, _ in GENDERS),
        choices=GENDERS,
        default=DO_NOT_SHOW,
    )

    status = models.CharField(
        max_length=max(len(x) for x, _ in STATUS),
        choices=STATUS,
        default=DO_NOT_SHOW,
    )

    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.candidate_first_name} {self.candidate_last_name}'


    class Meta:
        verbose_name = 'Interview'
