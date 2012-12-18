Configuring Django with stacktraces routed through Metlog
=========================================================

Integrating metlog into Django to capture stacktraces requires doing a
couple things.

1. Setup Raven+Django integration
2. Setup Metlog clients
3. Switch the standard Sentry client and instead use
   MetlogDjangoClient

Step 1
------

Setup the sentry client (raven) for use with Django.

Settings up raven is documented completely in the `raven-python
documentation <http://raven.readthedocs.org/en/latest/>`_, however the
following setup should get you up and running.

1.  Add raven.contrib.django to your INSTALLED_APPS in settings.py
2.  Set SENTRY_CLIENT to 'raven.contrib.django.DjangoClient' in settings.py

Here's what that'll look like in settings.py ::

    INSTALLED_APPS = (
        # You probably have more apps here
        'raven.contrib.django',
    )

    RAVEN_CONFIG = {
        # Forcing register_signals to True will make raven ignore the
        # DEBUG flag when trying to capture stack traces
        'register_signals': True,

        # The DSN should point to your Sentry instance.  See Sentry
        # documentation for details.
        'dsn': 'http://public:secret@example.com/1',
    }

    SENTRY_CLIENT = 'raven.contrib.django.DjangoClient'

The above settings should capture all stacktraes and route through the
standard raven client and send messages on to Sentry.

Step 2
------

Setup metlog with just the DebugCaptureSender.  Please refer to the full documentation on
`configuring Metlog <http://metlog-py.rtfd.org>`_ to get a production
setup.

Add the following to your settings.py ::

    METLOG_CONF = {
        'sender': {
            'class': 'metlog.senders.DebugCaptureSender',
        },
    }

    from metlog.config import client_from_dict_config
    METLOG = client_from_dict_config(METLOG_CONF)

Step 3
------

Reconfigure Raven to use metlog as it's underlying sentry client. Just
change the SENTRY_CLIENT setting in settings.py to use the alternate
SENTRY_CLIENT  ::

    SENTRY_CLIENT = 'djangoraven.metlog.MetlogDjangoClient'

At this point, you can safely remove the DSN entry in RAVEN_CONFIG.
The MetlogDjangoClient does not need it.  Final routing of your
stacktrace is handled by `logstash <http://logstash-metlog.rtfd.org/>`_
or `heka <http://heka.rtfd.org/>`_.

That's it!  Your raven messages will route through metlog.

See the test suite to see how you can inspect messages when you're
testing.
