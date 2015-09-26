import re
import time
import random
import datetime
import requests

from django.conf import settings
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db.utils import IntegrityError

from celery.task import Task, task
from apps.core import log as logging

import twython
from .models import Email

EMAILS = re.compile(r'[\w.-]+@[\w.-]+')
URLS = re.compile(r'((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)')
TWITTER_SHORTENED_URL = 't.co'

TEST_URL = 'http://pastebin.com/raw.php?i=Rr9DZJpt'

params = {
    'app_key': settings.TWITTER_APP_KEY,
    'app_secret': settings.TWITTER_APP_KEY_SECRET,
    'oauth_token': settings.TWITTER_ACCESS_TOKEN,
    'oauth_token_secret': settings.TWITTER_ACCESS_TOKEN_SECRET,
}

def pull_emails_from_url(url=TEST_URL):
    """ """
    logging.info(" --- pull_emails_from_url")
    r = requests.get(url)
    for email in EMAILS.findall(r.content):
        try:
            e,_ =Email.objects.get_or_create(email=email,reference_url=url)
            if _:
                print "NEW: {}".format(e)
            else:
                print "EXISTING: {}".format(e)
        except IntegrityError:
            pass
        
        
class pull_emails(Task):

    name = 'pull_emails'

    def run(self, **kwargs):
        logging.info(" --- pull_emails")
        print(" --- pull_emails")

        t = twython.Twython(**params)
        search = t.search(q='dumpmon', count=1000)

        tweets = search['statuses']
        for tweet in tweets:
            urls =  URLS.findall(tweet['text'])
            if len(urls) > 0:
                valid_urls_for_parsing = [u for u in urls[0] \
                        if TWITTER_SHORTENED_URL in u]
                for u in valid_urls_for_parsing:
                    pull_emails_from_url(u)