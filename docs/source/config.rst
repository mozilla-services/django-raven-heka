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

Settings up raven with metlog is documented completely in the `raven-python
documentation <http://raven.readthedocs.org/en/latest/>`.  To get the
extra integration with Django, you will need to do the following
steps:

1.  Add raven.contrib.django to your INSTALLED_APPS in settings.py
2.  Set SENTRY_CLIENT to 'raven.contrib.django.DjangoClient' in settings.py
3.  Set the SENTRY_DSN in settings.py

Here's what that'll look like in settings.py ::

    my_dsn = 'http://public:secret@example.com/1'

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
        'dsn': my_dsn
    }

    SENTRY_CLIENT = 'raven.contrib.django.DjangoClient'
    SENTRY_DSN = my_dsn

The above settings should capture all stacktraces and route through the
standard raven client and send messages on to Sentry.

Unforunately at this time, you will need to have the DSN configured in
both the RAVEN_CONFIG and the SENTRY_DSN entries in settings.py

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

Due to the way that raven sets a project_id variable for Sentry, you
will need to explicitly set the SENTRY_DSN setting ::

    SENTRY_DSN = "udp://your:dsn@goeshere.com:9001/2"

At this point, you can safely remove the DSN entry in RAVEN_CONFIG.
The MetlogDjangoClient does not need it.  Final routing of your
stacktrace is handled by `logstash <http://logstash-metlog.rtfd.org/>`_
or `heka <http://heka.rtfd.org/>`_.

That's it!  Your raven messages will route through metlog.

See the test suite to see how you can inspect messages when you're
testing.
