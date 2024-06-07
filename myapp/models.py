from django.db import models

# Create your models here.


class UserProfil(models.Model):
    firstname = models.CharField(
        max_length=50, null=True, blank=True, verbose_name="FirstName"
    )
    lastname = models.CharField(
        max_length=50, null=True, blank=True, verbose_name="LastName"
    )
    job_position = models.CharField(
        max_length=50, null=True, blank=True, verbose_name="Job Position"
    )
    bussines_area = models.CharField(
        max_length=50, null=True, blank=True, verbose_name="Bussines Area"
    )
    self_description = models.TextField(
        max_length=200, null=True, blank=True, verbose_name="Self Description"
    )
    job_expectation = models.TextField(
        max_length=200, null=True, blank=True, verbose_name="Job Expectation"
    )
    programming_lang = models.CharField(
        max_length=50, null=True, blank=True, verbose_name="Programming Language"
    )
    last_framework = models.CharField(
        max_length=50, null=True, blank=True, verbose_name="Last Comoany Framework"
    )
    last_post_experience = models.CharField(
        max_length=50, null=True, blank=True, verbose_name="Last Company Experience"
    )
    last_comp_name = models.CharField(
        max_length=50, null=True, blank=True, verbose_name="Last Company Name"
    )
    country = models.CharField(max_length=50, null=True, blank=True)
    phone_code = models.CharField(
        max_length=50, null=True, blank=True, verbose_name="Phone Code"
    )
    phone_number = models.CharField(
        max_length=50, null=True, blank=True, verbose_name="Phone Number"
    )
    email = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.firstname} | {self.lastname}"
