============
raven-metlog
============

.. image:: https://secure.travis-ci.org/mozilla-services/raven-metlog.png

raven-metlog is a set of plugins for the Raven client of Sentry to
enable routing of raven messages through metlog.

The advantage of doing so allows metlog to act as a centralized client
to route all logging messages.  This greatly simplifies testing as you
can always just query the metlog client to see what messages have been
sent. 

More information about how Mozilla Services is using Metlog (including what is
being used for a router and what endpoints are in use / planning to be used)
can be found on the relevant `spec page
<https://wiki.mozilla.org/Services/Sagrada/Metlog>`_.
