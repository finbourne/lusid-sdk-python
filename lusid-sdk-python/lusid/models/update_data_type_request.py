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


class UpdateDataTypeRequest(Model):
    """UpdateDataTypeRequest.

    :param type_value_range: Possible values include: 'Open', 'Closed'
    :type type_value_range: str or ~lusid.models.enum
    :param display_name:
    :type display_name: str
    :param description:
    :type description: str
    :param value_type: Possible values include: 'String', 'Int', 'Decimal',
     'DateTime', 'Boolean', 'Map', 'List', 'PropertyArray', 'Percentage',
     'BenchmarkType', 'Code', 'Id', 'Uri', 'ArrayOfIds',
     'ArrayOfTransactionAliases', 'ArrayofTransactionMovements',
     'ArrayofUnits', 'StringArray', 'CurrencyAndAmount', 'TradePrice',
     'UnitCreation', 'Currency', 'UserId', 'MetricValue'
    :type value_type: str or ~lusid.models.enum
    :param acceptable_values:
    :type acceptable_values: list[object]
    :param unit_schema: Possible values include: 'NoUnits', 'Basic',
     'Iso4217Currency'
    :type unit_schema: str or ~lusid.models.enum
    :param acceptable_units:
    :type acceptable_units: list[~lusid.models.CreateUnitDefinition]
    """

    _validation = {
        'type_value_range': {'required': True},
        'display_name': {'required': True},
        'description': {'required': True},
        'value_type': {'required': True},
    }

    _attribute_map = {
        'type_value_range': {'key': 'typeValueRange', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'value_type': {'key': 'valueType', 'type': 'str'},
        'acceptable_values': {'key': 'acceptableValues', 'type': '[object]'},
        'unit_schema': {'key': 'unitSchema', 'type': 'str'},
        'acceptable_units': {'key': 'acceptableUnits', 'type': '[CreateUnitDefinition]'},
    }

    def __init__(self, type_value_range, display_name, description, value_type, acceptable_values=None, unit_schema=None, acceptable_units=None):
        super(UpdateDataTypeRequest, self).__init__()
        self.type_value_range = type_value_range
        self.display_name = display_name
        self.description = description
        self.value_type = value_type
        self.acceptable_values = acceptable_values
        self.unit_schema = unit_schema
        self.acceptable_units = acceptable_units
