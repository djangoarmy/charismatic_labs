from django.db import models
from model_utils.models import TimeStampedModel

class ContactDetails(TimeStampedModel):
    contact_name = models.CharField(max_length=255, blank=True)
    contact_email = models.EmailField(max_length=255, blank=True)
    contact_subject = models.CharField(max_length=255, blank=True, null=True)
    contact_message = models.TextField(blank=True, null=True)