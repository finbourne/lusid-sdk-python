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


class CreatePropertyDataFormatRequest(Model):
    """CreatePropertyDataFormatRequest.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param scope:
    :type scope: str
    :param code:
    :type code: str
    :param format_type: Possible values include: 'Open', 'Closed'
    :type format_type: str or ~lusid.models.enum
    :param order:
    :type order: int
    :param display_name:
    :type display_name: str
    :param description:
    :type description: str
    :param value_type: Possible values include: 'String', 'Int', 'Decimal',
     'DateTime', 'Boolean', 'Map', 'List', 'PropertyArray', 'Percentage',
     'BenchmarkType', 'Code', 'Id', 'Uri', 'ArrayOfIds', 'ArrayOfTxnAliases',
     'ArrayofTxnMovements', 'ArrayofUnits', 'StringArray', 'CurrencyAndAmount',
     'TradePrice'
    :type value_type: str or ~lusid.models.enum
    :param acceptable_values:
    :type acceptable_values: list[object]
    :ivar unit_schema: Possible values include: 'NoUnits', 'Basic',
     'Iso4217Currency'
    :vartype unit_schema: str or ~lusid.models.enum
    :ivar acceptable_units:
    :vartype acceptable_units: list[~lusid.models.CreateUnitDefinition]
    """

    _validation = {
        'scope': {'required': True},
        'code': {'required': True},
        'format_type': {'required': True},
        'order': {'required': True},
        'display_name': {'required': True},
        'description': {'required': True},
        'value_type': {'required': True},
        'unit_schema': {'readonly': True},
        'acceptable_units': {'readonly': True},
    }

    _attribute_map = {
        'scope': {'key': 'scope', 'type': 'str'},
        'code': {'key': 'code', 'type': 'str'},
        'format_type': {'key': 'formatType', 'type': 'str'},
        'order': {'key': 'order', 'type': 'int'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'value_type': {'key': 'valueType', 'type': 'str'},
        'acceptable_values': {'key': 'acceptableValues', 'type': '[object]'},
        'unit_schema': {'key': 'unitSchema', 'type': 'str'},
        'acceptable_units': {'key': 'acceptableUnits', 'type': '[CreateUnitDefinition]'},
    }

    def __init__(self, scope, code, format_type, order, display_name, description, value_type, acceptable_values=None):
        super(CreatePropertyDataFormatRequest, self).__init__()
        self.scope = scope
        self.code = code
        self.format_type = format_type
        self.order = order
        self.display_name = display_name
        self.description = description
        self.value_type = value_type
        self.acceptable_values = acceptable_values
        self.unit_schema = None
        self.acceptable_units = None
