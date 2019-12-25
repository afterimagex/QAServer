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

# @Time    : 2019/12/25 0025 13:24
# @Author  : peichao.xu
# @Email   : xj563853580@outlook.com
# @File    : test_settings.py

# ==============================================================================

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from qaserver.settings import base
from qaserver.settings import develop

# import pytest
import logging

logging.basicConfig(level=logging.DEBUG)


class TestCase:
    def test_base(self):
        _settings = base.settings
        logging.debug(_settings)

    def test_develop(self):
        _settings = develop
        logging.debug(_settings)


if __name__ == '__main__':
    _settings = develop.settings
    logging.debug(_settings)
