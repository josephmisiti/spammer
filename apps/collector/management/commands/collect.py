from django.core.management.base import BaseCommand
from django.conf import settings

from apps.collector.tasks import pull_emails_from_url,pull_emails

class Command(BaseCommand):
    help = "My shiny new management command."

    def handle(self, *args, **options):
        """ """
        
        #pull_emails_from_url()
        settings.CELERY_ALWAYS_EAGER = True
        settings.CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
        pull_emails.apply_async(kwargs={}, queue='email_queue')