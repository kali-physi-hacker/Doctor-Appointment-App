from django import forms

from appointment.models.doctor import (
    Doctor, Education, Award, Membership, Registration, Experience, ClinicImage
)


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = "__all__"


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = "__all__"


class AwardForm(forms.ModelForm):
    class Meta:
        model = Award
        fields = "__all__"


class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = "__all__"


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = "__all__"


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = "__all__"


class ClinicImageForm(forms.ModelForm):
    class Meta:
        model = ClinicImage
        fields = "__all__"
