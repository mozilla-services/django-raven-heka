# ***** BEGIN LICENSE BLOCK *****
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

# The Initial Developer of the Original Code is the Mozilla Foundation.
# Portions created by the Initial Developer are Copyright (C) 2012
# the Initial Developer. All Rights Reserved.
#
# Contributor(s):
#   Rob Miller (rmiller@mozilla.com)
#   Victor Ng (vng@mozilla.com)
#
# ***** END LICENSE BLOCK *****
import os
from setuptools import setup, find_packages

version = '0.2'

README = """
django-raven-metlog is a set of plugins for the Raven client of Sentry
to enable routing of raven messages through metlog when you are
running a Django application.
"""


tests_require = [
    'Django>=1.2,<1.5',
    'django-nose',
    'nose',
    'metlog-py',
    'mock',
    'pep8',
    'raven',
]

setup(name='django-raven-metlog',
      version=version,
      description="Django+Raven+Meltog integration",
      long_description=README,
      keywords='django metlog raven sentry',
      author='Victor Ng',
      author_email='vng@mozilla.com',
      url='https://github.com/mozilla-services/django-raven-metlog',
      license='MPLv2.0',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=['docopt', 'raven', 'metlog-raven>=0.4'],
      tests_require=tests_require,
      extras_require={'test': tests_require},
      test_suite='runtests.runtests',
      classifiers=['License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
                   'Intended Audience :: Developers',
                   'Intended Audience :: System Administrators',
                   'Operating System :: OS Independent',
                   'Topic :: Software Development'
                   ],
      )
