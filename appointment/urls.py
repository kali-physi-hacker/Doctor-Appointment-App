from django.urls import path

from appointment.views.profile import doctor_profile, doctor_profile_update


urlpatterns = [
    path('profile/doctor/', doctor_profile, name="profile_doctor"),
    path('profile/update/', doctor_profile_update, name="profile_doctor_update"),
]