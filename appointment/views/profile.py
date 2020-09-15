from django.shortcuts import render, redirect
from django.contrib import messages

from appointment.forms.profile import (
    DoctorForm, EducationForm, ExperienceForm, MembershipForm, AwardForm, RegistrationForm,
    ClinicImageForm
)

from appointment.helpers import get_form_data

EDUCATION_FIELDS = ("degree", "college", "year_of_completion")
CLINIC_IMAGE_FIELDS = ("image",)
AWARD_FIELDS = ("name", "year")
EXPERIENCE_FIELDS = ("hospital_name", "from_date", "to_date", "designation")
MEMBERSHIP_FIELDS = ("name",)
REGISTRATION_FIELDS = ("name", "year")


def doctor_profile(request):
    """
    Return the profile page of the doctor
    :param request:
    :return:
    """
    template = "authentication/profile/doctor/doctor.html"
    form = DoctorForm()
    context = {
        "doctor_form": form,
        "clinic_image_form": ClinicImageForm(),
        "award_form": AwardForm(),
        "experience_form": ExperienceForm(),
        "membership_form": MembershipForm(),
        "registration_form": RegistrationForm()
    }
    return render(request, template, context)


def doctor_profile_update(request):
    """
    Update the profile page of the doctor and return the doctor profile page
    :param request:
    :return:
    """
    if request.method == "POST":
        doctor_form = DoctorForm(request.POST)
        clinic_image_form = ClinicImageForm(get_form_data(CLINIC_IMAGE_FIELDS))
        education_form = EducationForm(get_form_data(EDUCATION_FIELDS))
        award_form = AwardForm(get_form_data(AWARD_FIELDS))
        experience_form = ExperienceForm(get_form_data(EXPERIENCE_FIELDS))
        membership_form = MembershipForm(get_form_data(MEMBERSHIP_FIELDS))
        registration_form = RegistrationForm(get_form_data(REGISTRATION_FIELDS))

        if (
                doctor_form.is_valid() and clinic_image_form.is_valid() and education_form.is_valid() and
                award_form.is_valid() and experience_form.is_valid() and membership_form.is_valid() and
                registration_form.is_valid()
        ):
            doctor_form.save()
            clinic_image_form.save()
            education_form.save()
            award_form.save()
            experience_form.save()
            membership_form.save()
            registration_form.save()
        else:
            import pdb; pdb.set_trace()

        messages.success("Profile Updated Successfully")
        return redirect("profile_doctor")
