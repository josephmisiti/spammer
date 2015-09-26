from django.db import models

from model_utils.models import TimeStampedModel

class Email(TimeStampedModel):

    email = models.EmailField(max_length=254, unique=True)
    reference_url = models.URLField(null=True)

    def __unicode__(self):
        return "Email {email} {reference_url}".format(email=self.email,
                    reference_url=self.reference_url)

    class Meta:
        app_label = 'collector'
        db_table = "emails"
        ordering = ['created']