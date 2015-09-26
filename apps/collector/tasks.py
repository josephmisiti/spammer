import time
import random
import datetime
import facebook

from django.conf import settings
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from celery.task import Task, task
from apps.core import log as logging

from .models import Email

class pull_emails(Task):

	name = 'pull_emails'

	def run(self, **kwargs):
		logging.info(" --- pull_emails")
