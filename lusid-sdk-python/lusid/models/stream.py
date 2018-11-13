# coding=utf-8
# --------------------------------------------------------------------------
# Copyright © 2018 FINBOURNE TECHNOLOGY LTD
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Stream(Model):
    """Stream.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar can_read:
    :vartype can_read: bool
    :ivar can_seek:
    :vartype can_seek: bool
    :ivar can_timeout:
    :vartype can_timeout: bool
    :ivar can_write:
    :vartype can_write: bool
    :ivar length:
    :vartype length: long
    :param position:
    :type position: long
    :param read_timeout:
    :type read_timeout: int
    :param write_timeout:
    :type write_timeout: int
    """

    _validation = {
        'can_read': {'readonly': True},
        'can_seek': {'readonly': True},
        'can_timeout': {'readonly': True},
        'can_write': {'readonly': True},
        'length': {'readonly': True},
    }

    _attribute_map = {
        'can_read': {'key': 'canRead', 'type': 'bool'},
        'can_seek': {'key': 'canSeek', 'type': 'bool'},
        'can_timeout': {'key': 'canTimeout', 'type': 'bool'},
        'can_write': {'key': 'canWrite', 'type': 'bool'},
        'length': {'key': 'length', 'type': 'long'},
        'position': {'key': 'position', 'type': 'long'},
        'read_timeout': {'key': 'readTimeout', 'type': 'int'},
        'write_timeout': {'key': 'writeTimeout', 'type': 'int'},
    }

    def __init__(self, position=None, read_timeout=None, write_timeout=None):
        super(Stream, self).__init__()
        self.can_read = None
        self.can_seek = None
        self.can_timeout = None
        self.can_write = None
        self.length = None
        self.position = position
        self.read_timeout = read_timeout
        self.write_timeout = write_timeout
