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


class UpdatePropertyDataFormatRequest(Model):
    """UpdatePropertyDataFormatRequest.

    :param format_type: Possible values include: 'Basic', 'Limited',
     'Currency'
    :type format_type: str or ~lusid.models.enum
    :param order:
    :type order: int
    :param display_name:
    :type display_name: str
    :param value_type: Possible values include: 'String', 'Int', 'Decimal',
     'DateTime', 'Boolean', 'Map', 'PropertyArray', 'Percentage', 'Currency',
     'BenchmarkType', 'Code', 'Id', 'Uri', 'ArrayOfIds', 'ArrayOfTxnAliases',
     'ArrayofTxnMovements'
    :type value_type: str or ~lusid.models.enum
    :param acceptable_values:
    :type acceptable_values: list[object]
    """

    _validation = {
        'format_type': {'required': True},
        'order': {'required': True},
        'display_name': {'required': True},
        'value_type': {'required': True},
    }

    _attribute_map = {
        'format_type': {'key': 'formatType', 'type': 'str'},
        'order': {'key': 'order', 'type': 'int'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'value_type': {'key': 'valueType', 'type': 'str'},
        'acceptable_values': {'key': 'acceptableValues', 'type': '[object]'},
    }

    def __init__(self, format_type, order, display_name, value_type, acceptable_values=None):
        super(UpdatePropertyDataFormatRequest, self).__init__()
        self.format_type = format_type
        self.order = order
        self.display_name = display_name
        self.value_type = value_type
        self.acceptable_values = acceptable_values
