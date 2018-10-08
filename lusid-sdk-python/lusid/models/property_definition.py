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


class PropertyDefinition(Model):
    """PropertyDefinition.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param href:
    :type href: str
    :param key:
    :type key: str
    :param value_type: Possible values include: 'String', 'Int', 'Decimal',
     'DateTime', 'Boolean', 'Map', 'List', 'PropertyArray', 'Percentage',
     'BenchmarkType', 'Code', 'Id', 'Uri', 'ArrayOfIds',
     'ArrayOfTransactionAliases', 'ArrayofTransactionMovements',
     'ArrayofUnits', 'StringArray', 'CurrencyAndAmount', 'TradePrice',
     'UnitCreation', 'Currency', 'UserId', 'MetricValue'
    :type value_type: str or ~lusid.models.enum
    :param value_required:
    :type value_required: bool
    :param display_name:
    :type display_name: str
    :param data_type_id:
    :type data_type_id: ~lusid.models.ResourceId
    :param life_time: Possible values include: 'Perpetual', 'TimeVariant'
    :type life_time: str or ~lusid.models.enum
    :param type: Possible values include: 'Label', 'Metric'
    :type type: str or ~lusid.models.enum
    :param unit_schema: Possible values include: 'NoUnits', 'Basic',
     'Iso4217Currency'
    :type unit_schema: str or ~lusid.models.enum
    :ivar domain: Possible values include: 'Trade', 'Portfolio', 'Security',
     'Holding', 'ReferenceHolding', 'TxnType'
    :vartype domain: str or ~lusid.models.enum
    :ivar scope:
    :vartype scope: str
    :ivar code:
    :vartype code: str
    :param links:
    :type links: list[~lusid.models.Link]
    """

    _validation = {
        'domain': {'readonly': True},
        'scope': {'readonly': True},
        'code': {'readonly': True},
    }

    _attribute_map = {
        'href': {'key': 'href', 'type': 'str'},
        'key': {'key': 'key', 'type': 'str'},
        'value_type': {'key': 'valueType', 'type': 'str'},
        'value_required': {'key': 'valueRequired', 'type': 'bool'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'data_type_id': {'key': 'dataTypeId', 'type': 'ResourceId'},
        'life_time': {'key': 'lifeTime', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'unit_schema': {'key': 'unitSchema', 'type': 'str'},
        'domain': {'key': 'domain', 'type': 'str'},
        'scope': {'key': 'scope', 'type': 'str'},
        'code': {'key': 'code', 'type': 'str'},
        'links': {'key': 'links', 'type': '[Link]'},
    }

    def __init__(self, href=None, key=None, value_type=None, value_required=None, display_name=None, data_type_id=None, life_time=None, type=None, unit_schema=None, links=None):
        super(PropertyDefinition, self).__init__()
        self.href = href
        self.key = key
        self.value_type = value_type
        self.value_required = value_required
        self.display_name = display_name
        self.data_type_id = data_type_id
        self.life_time = life_time
        self.type = type
        self.unit_schema = unit_schema
        self.domain = None
        self.scope = None
        self.code = None
        self.links = links
