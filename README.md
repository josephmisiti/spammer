### Introduction

Spammer is a tool for collecting compromised email address. I built this app
for fun, to see how many email address could be collecting by just letting it run for a few months.

The email are currently collect from the follower twitter feed:

https://twitter.com/dumpmon

### Usage:

First clone the project:

```
git clone git@github.com:josephmisiti/spammer.git
```

Next, install the requirements:

```
bin/install
```

Next, create a `local_settings.py` file:

```
cp spammer/local_settings.dev spammer/local_settings.py
```

Next, create an application on Twitter, and replace the following in `settings.py`

```
TWITTER_APP_KEY = 'xxxx'
TWITTER_APP_KEY_SECRET = 'xxxx'
TWITTER_ACCESS_TOKEN = 'xxxx'
TWITTER_ACCESS_TOKEN_SECRET = 'xxxx'
```

Next, setup your database

```
python manage.py syncdb
python manage.py migrate
```

Finally run `collect` and watch the email address fly in:

```
(spammer)JOSEPH-MISITI:spammer josephmisiti$ ./manage.py collect | more
 --- pull_emails
EXISTING: Email arshiarashedzadeh11@gmail.com http://t.co/d04m9WUPyO
EXISTING: Email pipergecko@gmail.com http://t.co/d04m9WUPyO
EXISTING: Email valden1@google.com http://t.co/d04m9WUPyO
EXISTING: Email nicknuckolls@yahoo.com http://t.co/d04m9WUPyO
EXISTING: Email firmlygraspmybre-wait@gmail.com http://t.co/d04m9WUPyO
EXISTING: Email tylermwrussell321@yahoo.com http://t.co/d04m9WUPyO
EXISTING: Email Sameasmyemail@outlook.com http://t.co/d04m9WUPyO
EXISTING: Email aidsterlav13@gmail.com http://t.co/d04m9WUPyO
EXISTING: Email mason.phillips@ousd.us http://t.co/d04m9WUPyO
EXISTING: Email yipeng@live.ca http://t.co/d04m9WUPyO
EXISTING: Email jjjjjjjjjjjjjjjjjjj@myass.com http://t.co/d04m9WUPyO
EXISTING: Email floopernugget@gmail.com http://t.co/d04m9WUPyO
EXISTING: Email mohammad_atieh7@live.com http://t.co/d04m9WUPyO
EXISTING: Email gwilliam@nl.rogers.com http://t.co/d04m9WUPyO
EXISTING: Email kennyvu03212002@gmail.com http://t.co/d04m9WUPyO
EXISTING: Email justin.echeverria0717@gmail.com http://t.co/d04m9WUPyO
EXISTING: Email blaizegallant@eastlink.ca http://t.co/d04m9WUPyO
EXISTING: Email Ishmael1212835@me.com http://t.co/d04m9WUPyO
EXISTING: Email linktompkins@gmail.com http://t.co/d04m9WUPyO
EXISTING: Email rjsolis22@yahoo.com http://t.co/d04m9WUPyO
EXISTING: Email youaregay@stupidgays.com.gay http://t.co/d04m9WUPyO
EXISTING: Email tbrod13371@gmail.com http://t.co/d04m9WUPyO
EXISTING: Email Johnmarone633@gmail.com http://t.co/d04m9WUPyO
EXISTING: Email coolsegraal@yahoo.com http://t.co/d04m9WUPyO
EXISTING: Email fireboy123@live.com http://t.co/d04m9WUPyO
EXISTING: Email lol@gmail.com http://t.co/d04m9WUPyO
EXISTING: Email PvzItsAboutTime@gmail.com http://t.co/d04m9WUPyO
EXISTING: Email caitlync2003@yahoo.com http://t.co/d04m9WUPyO
EXISTING: Email jordanjohnson47@yahoo.com http://t.co/d04m9WUPyO
EXISTING: Email clareforbes@live.co.uk http://t.co/d04m9WUPyO
EXISTING: Email kristanovak93@yahoo.com http://t.co/d04m9WUPyO
```

I ran it once and collected over 21K+ email address in on sitting!

```
spammer=# SELECT COUNT(*) from emails;
 count
-------
 21139
(1 row)
```

If you setup a celery queue, the project is setup to run a cron-job every 24 hours

```
CELERYBEAT_SCHEDULE = {
    'pull_emails': {
        'task':     'pull_emails',
        "schedule"    : timedelta(seconds=60*60*24),
        'options'    : {'queue': 'email_queue' },
    },
}
```
