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

__version__ = '0.1.0'

import hashlib
from pathlib import Path


def generate_hashes(dirpath: 'PathLike',
                    hashfunc=hashlib.blake2b,
                    extension='.blake2b'):
    """Generate hashes recursively for a directory."""
    dirpath = Path(dirpath)
    for path in dirpath.glob('**/*'):
        if not path.is_file():
            continue
        h = hashfunc()
        with path.open('rb') as f:
            _feed_hash(h, f)
        hpath = path.parent / (path.name + extension)
        with hpath.open('w') as f:
            f.write(h.hexdigest())
            f.write('\n')


def _feed_hash(hash, file, blocksize=8192):
    """Feed a binary file to a hash object."""
    while True:
        d = file.read(blocksize)
        if not d:
            return
        hash.update(d)
