#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# @Time    : 2019/12/24 0024 15:13
# @Author  : peichao.xu
# @Email   : xj563853580@outlook.com
# @File    : server.py

# ==============================================================================

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import click
import os
import sys
import tornado.web

from importlib import import_module
from logging.config import dictConfig
from raven.contrib.tornado import AsyncSentryClient
from qaserver.handlers.urls import urls


def make_app(debug=None):
    assert isinstance(urls, (list, tuple)), 'urls must be list or tuple'
    return tornado.web.Application(urls, debug=debug)


@click.command()
@click.option('--port', default=9090, help='The port of server.')
@click.option('--profile', default='develop', help='The profile.')
def run_app(port, profile):
    settings = import_module(f'qaserver.settings.{profile}').settings
    tornado.settings = settings
    dictConfig(tornado.settings.LOGGING)
    app = make_app(settings.DEBUG)
    app.listen(port)
    app.sentry_client = AsyncSentryClient(
        '<sentry>'
    )
    sys.stdout.write(f"Start server at:http://0.0.0.0:{port} \nProfile: {profile}\n")
    tornado.ioloop.IOLoop.current().start()
