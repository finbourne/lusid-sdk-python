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

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar property_key: The Side
    :vartype property_key: str
    :ivar map_from: The Side
    :vartype map_from: str
    :ivar set_to: The Side
    :vartype set_to: object
    """

    _validation = {
        'property_key': {'required': True, 'readonly': True},
        'map_from': {'readonly': True},
        'set_to': {'readonly': True},
    }

    _attribute_map = {
        'property_key': {'key': 'propertyKey', 'type': 'str'},
        'map_from': {'key': 'mapFrom', 'type': 'str'},
        'set_to': {'key': 'setTo', 'type': 'object'},
    }

    def __init__(self):
        super(TxnPropertyMappingDto, self).__init__()
        self.property_key = None
        self.map_from = None
        self.set_to = None
