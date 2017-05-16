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

import argparse
import sys

from mir.steiner import commands


def main(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=commands.COMMANDS)
    parser.add_argument('command_args', nargs=argparse.REMAINDER)
    args = parser.parse_args(args)
    cmd = commands.COMMANDS[args.command]
    return cmd(args.command_args)


if __name__ == '__main__':
    sys.exit(main())
