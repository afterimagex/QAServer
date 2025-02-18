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

# @Time    : 2019/12/24 0024 12:45
# @Author  : peichao.xu
# @Email   : xj563853580@outlook.com
# @File    : __init__.py

# ==============================================================================

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os

settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), '../templates'),
    static_path=os.path.join(os.path.dirname(__file__), '../static'),
    xsrf_cookies=True,
    cookie_secret='RYxFqFQyRCiCZ/nxFfTMCrbqZpRZ5UW9tQ86fKvrfIw=',
    debug=True,
    static_url_prefix='/static/',
)
