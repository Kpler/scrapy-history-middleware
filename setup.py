# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils import setup

import history


packages = [
    'history',
]

requires = [
    'scrapy',
    'boto',
    'parsedatetime',
]

setup(
    name='scrapyhistory',
    version=history.__version__,
    description='Scrapy downloader middleware to enable persistent storage.',
    author='Andrew Preston',
    author_email='andrew@preston.co.nz',
    url='http://github.com/playandbuild/scrapy-history-middleware',
    packages=packages,
    install_requires=requires,
    classifiers=(
        'Development Status :: 4 - Beta'
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
    ),
)
