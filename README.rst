=================
django-raven-heka
=================

.. image:: https://secure.travis-ci.org/mozilla-services/django-raven-heka.png

django-raven-heka is a set of plugins for the Raven client
to enable routing of raven messages through heka when you are
running a Django application.

The primary use of this is to standardize heka integration into
`Playdoh <http://playdoh.readthedocs.org/>`_ applications.

The advantage of doing so allows heka to act as a centralized client
to route all logging messages.  This greatly simplifies testing as you
can always just query the heka client to see what messages have been
sent.
