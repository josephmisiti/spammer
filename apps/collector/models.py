from django.db import models

from model_utils.models import TimeStampedModel

class Emails(TimeStampedModel):

	email = models.EmailField(max_length=254, unique=True)

	class Meta:
		app_label = 'collector'
		db_table = "emails"
		ordering = ['created']