# Copyright (C) 2017 Allen Li
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

import contextlib
import io

from mir.steiner import ahiru


def test_quack():
    assert ahiru.quack() == 'quack'


def test_main():
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        ahiru.main()
    assert output.getvalue() == 'quack\n'


def test_main_with_args():
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        ahiru.main([])
    assert output.getvalue() == 'quack\n'
