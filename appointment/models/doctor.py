from django.db import models
from django.core.validators import RegexValidator
from django_countries.fields import CountryField
from django.contrib.auth import get_user_model

from appointment.helpers import get_file_name_ext, generate_random_text
from appointment.constants.doctor import DOCTOR_DEGREE_OPTIONS


User = get_user_model()


def doctor_image_upload_path(instance, file_path):
    """
    Return an upload path for saving doctor profile photos
    :param instance:
    :param file_path:
    :return:
    """
    file_name, file_ext = get_file_name_ext(file_path)
    random_file_name = generate_random_text(file_name)
    final_file_name = f"profile_photos/{random_file_name}"
    return final_file_name


class Doctor(models.Model):

    # Gender Options
    MALE = 'M'
    FEMALE = 'F'

    GENDER_OPTIONS = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    # Pricing Options
    FREE = 'F'
    CUSTOM_PRICE = 'CP'
    PRICING_OPTIONS = (
        (FREE, 'Free'),
        (CUSTOM_PRICE, 'CUSTOM PRICE'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=doctor_image_upload_path, null=True, blank=True)

    phone_validator = RegexValidator(
        regex=r'^\+?\d(9,15)$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone_number = models.CharField(validators=(phone_validator,), max_length=17, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_OPTIONS, null=True, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    biography = models.TextField(blank=True, null=True)

    clinic_name = models.CharField(max_length=200, null=True, blank=True)
    clinic_address = models.CharField(max_length=200, null=True, blank=True)
    address_line_one = models.CharField(max_length=200, null=True, blank=True)
    address_line_two = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    country = CountryField(default='GH')
    postal_code = models.CharField(max_length=5, null=True, blank=True)

    pricing = models.CharField(max_length=2, choices=PRICING_OPTIONS, default=FREE, null=True, blank=True)

    services = models.TextField(null=True, blank=True)
    specialization = models.TextField(null=True, blank=True)

    activated = models.BooleanField(default=False)


def clinic_image_file_path(instance, file_path):
    """
    Return a string for clinic image upload
    :param instance:
    :param file_path:
    :return:
    """
    file_name, file_ext = get_file_name_ext(file_path)
    random_file_name = generate_random_text(file_name)
    final_file_name = f"clinic/{random_file_name}"
    return final_file_name


class ClinicImage(models.Model):
    image = models.ImageField(upload_to=clinic_image_file_path)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)


class Education(models.Model):

    degree = models.CharField(max_length=15, choices=DOCTOR_DEGREE_OPTIONS)
    college = models.CharField(max_length=200)
    year_of_completion = models.PositiveIntegerField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.college} - {self.degree} - {self.year_of_completion}"


class Award(models.Model):
    name = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)


class Experience(models.Model):
    hospital_name = models.CharField(max_length=200)
    from_date = models.DateField()
    to_date = models.DateField()
    designation = models.TextField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)


class Membership(models.Model):
    name = models.CharField(max_length=200)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)


class Registration(models.Model):
    name = models.CharField(max_length=200)
    year = models.DateField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
