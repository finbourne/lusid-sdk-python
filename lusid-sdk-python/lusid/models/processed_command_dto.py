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


class ProcessedCommandDto(Model):
    """ProcessedCommandDto.

    :param description:
    :type description: str
    :param path:
    :type path: str
    :param user_id: The user that issued the command.
    :type user_id: str
    :param processed_time: The as at time of the events published by the
     processing of
     this command.
    :type processed_time: object
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'path': {'key': 'path', 'type': 'str'},
        'user_id': {'key': 'userId', 'type': 'str'},
        'processed_time': {'key': 'processedTime', 'type': 'object'},
    }

    def __init__(self, description=None, path=None, user_id=None, processed_time=None):
        super(ProcessedCommandDto, self).__init__()
        self.description = description
        self.path = path
        self.user_id = user_id
        self.processed_time = processed_time
