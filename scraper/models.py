from django.db import models


class Company(models.Model):
    abbr = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    revenue = models.IntegerField(blank=True, null=True)
    site = models.URLField(blank=True, null=True)
    street_address1 = models.CharField(max_length=255, blank=True, null=True)
    street_address2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    number_of_employee = models.IntegerField(blank=True, null=True)
    industry = models.CharField(max_length=255, blank=True, null=True)
