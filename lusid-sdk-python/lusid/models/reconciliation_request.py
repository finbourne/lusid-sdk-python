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


class ReconciliationRequest(Model):
    """ReconciliationRequest.

    :param left_scope:
    :type left_scope: str
    :param left_code:
    :type left_code: str
    :param left_effective_at:
    :type left_effective_at: datetime
    :param left_as_at:
    :type left_as_at: datetime
    :param right_scope:
    :type right_scope: str
    :param right_code:
    :type right_code: str
    :param right_effective_at:
    :type right_effective_at: datetime
    :param right_as_at:
    :type right_as_at: datetime
    """

    _attribute_map = {
        'left_scope': {'key': 'leftScope', 'type': 'str'},
        'left_code': {'key': 'leftCode', 'type': 'str'},
        'left_effective_at': {'key': 'leftEffectiveAt', 'type': 'iso-8601'},
        'left_as_at': {'key': 'leftAsAt', 'type': 'iso-8601'},
        'right_scope': {'key': 'rightScope', 'type': 'str'},
        'right_code': {'key': 'rightCode', 'type': 'str'},
        'right_effective_at': {'key': 'rightEffectiveAt', 'type': 'iso-8601'},
        'right_as_at': {'key': 'rightAsAt', 'type': 'iso-8601'},
    }

    def __init__(self, left_scope=None, left_code=None, left_effective_at=None, left_as_at=None, right_scope=None, right_code=None, right_effective_at=None, right_as_at=None):
        super(ReconciliationRequest, self).__init__()
        self.left_scope = left_scope
        self.left_code = left_code
        self.left_effective_at = left_effective_at
        self.left_as_at = left_as_at
        self.right_scope = right_scope
        self.right_code = right_code
        self.right_effective_at = right_effective_at
        self.right_as_at = right_as_at
