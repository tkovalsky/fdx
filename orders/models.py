import datetime

from django.conf import settings
from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.urls import reverse


class Contact(TimeStampedModel):
    name = models.CharField(max_length=60, null=False, blank=False)
    company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True, blank=True)
    email_address = models.EmailField(null=True, blank=True)
    linkedin_profile_url = models.URLField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    extension = models.CharField(max_length=5, null=True, blank=True)
    last_contact_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
         """
         Returns the url to access a contact.
         """
         return reverse('contact-detail', args=[str(self.id)])

    class Meta:
        ordering = ["name"]


class Company(TimeStampedModel):
    name = models.CharField(max_length=30, null=False, blank=False)

    BUSINESS_TYPE = (
        ('elect', 'Electrician'),
        ('plumb', 'Plumber'),
        ('hvac', 'HVAC'),
        ('re', 'Real Estate'),
        ('uncls', 'Not Classified'),
    )

    type_of_business = models.CharField(max_length=5, choices=BUSINESS_TYPE, blank=True, default='uncls', help_text="Business type")

    web_site_url = models.URLField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email_composition = models.CharField(max_length=50, null=True, blank=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
         """
         Returns the url to access a company.
         """
         return reverse('sale-detail', args=[str(self.id)])

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "companies"

class Touch(TimeStampedModel):
    contact = models.ForeignKey('Contact', on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField(auto_now=True, auto_now_add=False)
    touch_type = models.CharField(max_length=20) #add a reference for a dropdown selector
    follow_up_days = models.PositiveIntegerField(default=0)
    follow_up_date = models.CharField(max_length=20, null=True, blank=True) #add a reference for a dropdown selector

    def __str__(self):
        return "%s - %s" % (self.date, self.touch_type)

    def get_absolute_url(self):
         """
         Returns the url to access a particular touch.
         """
         return reverse('touch-detail', args=[str(self.id)])

    class Meta:
        verbose_name_plural = "touches"


class Note(TimeStampedModel):
    contact = models.ForeignKey('Contact', on_delete=models.SET_NULL, null=True, blank=True)
    company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True, blank=True)
    note = models.TextField()

    def __str__(self):
        return "%s - %s - %s" % (self.contact, self.company, self.note )

    def get_absolute_url(self):
         """
         Returns the url to access a particular note.
         """
         return reverse('note-detail', args=[str(self.id)])

class Opportunity(TimeStampedModel):
    date = models.DateField(auto_now=True, auto_now_add=False)
    name = models.CharField(max_length=50) #add a reference for a dropdown selector
    url = models.URLField(blank=True, null=True)
    company = models.ForeignKey('Company', blank=True, null=True)
    notes = models.ForeignKey('Note', blank=True, null=True)
    detail = models.TextField()

    def __str__(self):
        return "%s - %s - %s" % (self.date, self.name, self.company)

    def get_absolute_url(self):
         """
         Returns the url to access a particular touch.
         """
         return reverse('touch-detail', args=[str(self.id)])

    class Meta:
        verbose_name_plural = "opportunities"
