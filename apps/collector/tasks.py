import re
import time
import random
import datetime
import requests

from django.conf import settings
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from celery.task import Task, task
from apps.core import log as logging

import twython
from .models import Email

EMAILS = re.compile(r'[\w.-]+@[\w.-]+')

TEST_URL = 'http://pastebin.com/raw.php?i=Rr9DZJpt'

def pull_emails_from_url(url=TEST_URL):
    """ """
    logging.info(" --- pull_emails_from_url")
    r = requests.get(url)
    for email in EMAILS.findall(r.content):
        e,_ =Email.objects.get_or_create(email=email,reference_url=url)
        print e
        
        
class pull_emails(Task):

    name = 'pull_emails'

    def run(self, **kwargs):
        logging.info(" --- pull_emails")

        t = twython.Twython(app_key=settings.TWITTER_APP_KEY,
        app_secret=settings.TWITTER_APP_KEY_SECRET,
        oauth_token=settings.TWITTER_ACCESS_TOKEN,
        oauth_token_secret=settings.TWITTER_ACCESS_TOKEN_SECRET)

        search = t.search(q='#teaparty', count=1000)

        tweets = search['statuses']

        for tweet in tweets:
            print tweet['id_str'], '\n', tweet['text'], '\n\n\n'