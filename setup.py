# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from setuptools import setup

import history


install_requires = [
    'boto==2.47.0',
    'parsedatetime==1.4',
    'Scrapy==1.5.0',
]

setup(
    name=history.__package__,
    version=history.__version__,
    description='Scrapy downloader middleware to enable persistent storage.',
    author='Andrew Preston',
    author_email='andrew@preston.co.nz',
    url='http://github.com/Kpler/scrapy-history-middleware',
    packages=['history'],
    install_requires=install_requires,
)
