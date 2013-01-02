# ***** BEGIN LICENSE BLOCK *****
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# The Initial Developer of the Original Code is the Mozilla Foundation.
# Portions created by the Initial Developer are Copyright (C) 2012
# the Initial Developer. All Rights Reserved.
#
# Contributor(s):
#   Victor Ng (vng@mozilla.com)
#
# ***** END LICENSE BLOCK *****

from __future__ import absolute_import
from raven.base import Client
from raven.contrib.django.client import DjangoClient

try:
    from django.conf import settings
    from metlog.client import SEVERITY
except:
    settings = None  # NOQA
    SEVERITY = None  # NOQA

class MetlogDjangoClient(DjangoClient):
    """
    This client simply overrides the send_encoded method in the base
    Client so that we use settings.METLOG for transmission
    """

    def is_enabled(self):
        return True

    def send(self, **kwargs):
        """
        Serializes and signs ``data`` and passes the payload off to ``send_remote``

        raven.contrib.django.client.DjangoClient does a check for
        self.servers, just bypass that and delegate to the primary
        raven.base.Client base class which will juse encode and fwd
        the data on to send_encoded.
        """

        return Client.send(self, **kwargs)

    def send_encoded(self, message, public_key=None, \
            auth_header=None, **kwargs):
        """
        Given an already serialized message send it off to metlog
        """
        settings.METLOG.raven(payload=message)
