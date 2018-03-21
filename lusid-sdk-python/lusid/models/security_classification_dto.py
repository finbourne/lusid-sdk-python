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


class SecurityClassificationDto(Model):
    """SecurityClassificationDto.

    :param uid: Unique security identifier
    :type uid: str
    :param effective_from: Date from which this classification is effective
    :type effective_from: datetime
    :param properties:
    :type properties: list[~lusid.models.PropertyDto]
    """

    _attribute_map = {
        'uid': {'key': 'uid', 'type': 'str'},
        'effective_from': {'key': 'effectiveFrom', 'type': 'iso-8601'},
        'properties': {'key': 'properties', 'type': '[PropertyDto]'},
    }

    def __init__(self, uid=None, effective_from=None, properties=None):
        super(SecurityClassificationDto, self).__init__()
        self.uid = uid
        self.effective_from = effective_from
        self.properties = properties
