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
import tornado

from importlib import import_module
from logging.config import dictConfig
from raven.contrib.tornado import AsyncSentryClient


def make_app(debug=None):
    pass

@click.command()
@click.option('--port', default=9090)
@click.option('--profile', default='develop')
def main(port, profile):
    settings = import_module(f'qaserver.settings.{profile}')
    tornado.settings = settings
    app = make_app(settings.DEBUG)
    app.sentry_client = AsyncSentryClient(
        '<sentry>'
    )
    sys.stdout.write(f"Start server at:http://0.0.0.0:{port} \nProfile: {profile}\n")
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    # current_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # sys.path.insert(0, current_path)
    main()
