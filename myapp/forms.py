from django.forms import ModelForm, TextInput
from .models import *


class UserProfilForm(ModelForm):

    class Meta:
        model = UserProfil
        fields = (
            "firstname",
            "lastname",
            "job_position",
            "bussines_area",
            "self_description",
            "job_expectation",
            "programming_lang",
            "last_framework",
            "last_post_experience",
            "last_comp_name",
            "country",
            "phone_code",
            "phone_number",
            "email",
        )
        widgets = {
            "firstname": TextInput(attrs={"class": "input"}),
            "lastname": TextInput(attrs={"class": "input"}),
            "job_position": TextInput(attrs={"class": "input"}),
            "bussines_area": TextInput(attrs={"class": "input"}),
            "self_description": TextInput(attrs={"class": "input"}),
            "job_expectation": TextInput(attrs={"class": "input"}),
            "programming_lang": TextInput(attrs={"class": "input"}),
            "last_framework": TextInput(attrs={"class": "input"}),
            "last_post_experience": TextInput(attrs={"class": "input"}),
            "last_comp_name": TextInput(attrs={"class": "input"}),
            "country": TextInput(attrs={"class": "input"}),
            "phone_code": TextInput(attrs={"class": "input"}),
            "phone_number": TextInput(attrs={"class": "input"}),
            "email": TextInput(attrs={"class": "input"}),
        }
