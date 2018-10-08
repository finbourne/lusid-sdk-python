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


class FieldSchema(Model):
    """FieldSchema.

    :param scope:
    :type scope: str
    :param name:
    :type name: str
    :param display_name:
    :type display_name: str
    :param type: Possible values include: 'String', 'Int', 'Decimal',
     'DateTime', 'Boolean', 'Map', 'List', 'PropertyArray', 'Percentage',
     'BenchmarkType', 'Code', 'Id', 'Uri', 'ArrayOfIds',
     'ArrayOfTransactionAliases', 'ArrayofTransactionMovements',
     'ArrayofUnits', 'StringArray', 'CurrencyAndAmount', 'TradePrice',
     'UnitCreation', 'Currency', 'UserId', 'MetricValue'
    :type type: str or ~lusid.models.enum
    :param is_metric:
    :type is_metric: bool
    :param display_order:
    :type display_order: int
    :param property_schema:
    :type property_schema: dict[str, ~lusid.models.FieldSchema]
    """

    _attribute_map = {
        'scope': {'key': 'scope', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'is_metric': {'key': 'isMetric', 'type': 'bool'},
        'display_order': {'key': 'displayOrder', 'type': 'int'},
        'property_schema': {'key': 'propertySchema', 'type': '{FieldSchema}'},
    }

    def __init__(self, scope=None, name=None, display_name=None, type=None, is_metric=None, display_order=None, property_schema=None):
        super(FieldSchema, self).__init__()
        self.scope = scope
        self.name = name
        self.display_name = display_name
        self.type = type
        self.is_metric = is_metric
        self.display_order = display_order
        self.property_schema = property_schema
