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


class TxnPropertyMappingDto(Model):
    """TxnPropertyMappingDto.

    :param property_key: The Side
    :type property_key: str
    :param map_from: The Side
    :type map_from: str
    :param set_to: The Side
    :type set_to: object
    """

    _validation = {
        'property_key': {'required': True},
    }

    _attribute_map = {
        'property_key': {'key': 'propertyKey', 'type': 'str'},
        'map_from': {'key': 'mapFrom', 'type': 'str'},
        'set_to': {'key': 'setTo', 'type': 'object'},
    }

    def __init__(self, property_key, map_from=None, set_to=None):
        super(TxnPropertyMappingDto, self).__init__()
        self.property_key = property_key
        self.map_from = map_from
        self.set_to = set_to
