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


class PropertyDefinitionDto(Model):
    """PropertyDefinitionDto.

    :param href:
    :type href: str
    :param key:
    :type key: str
    :param value_type: Possible values include: 'String', 'Int', 'Decimal',
     'DateTime', 'Boolean', 'Map', 'List', 'PropertyArray', 'Percentage',
     'BenchmarkType', 'Code', 'Id', 'Uri', 'ArrayOfIds', 'ArrayOfTxnAliases',
     'ArrayofTxnMovements', 'ArrayofUnits', 'StringArray', 'CurrencyAndAmount',
     'TradePrice'
    :type value_type: str or ~lusid.models.enum
    :param value_required:
    :type value_required: bool
    :param display_name:
    :type display_name: str
    :param data_format_id:
    :type data_format_id: ~lusid.models.ResourceId
    :param sort:
    :type sort: str
    :param life_time: Possible values include: 'Perpetual', 'TimeVariant'
    :type life_time: str or ~lusid.models.enum
    :param type: Possible values include: 'Label', 'Metric'
    :type type: str or ~lusid.models.enum
    :param unit_schema: Possible values include: 'NoUnits', 'Basic',
     'Iso4217Currency'
    :type unit_schema: str or ~lusid.models.enum
    :param _links:
    :type _links: list[~lusid.models.Link]
    """

    _attribute_map = {
        'href': {'key': 'href', 'type': 'str'},
        'key': {'key': 'key', 'type': 'str'},
        'value_type': {'key': 'valueType', 'type': 'str'},
        'value_required': {'key': 'valueRequired', 'type': 'bool'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'data_format_id': {'key': 'dataFormatId', 'type': 'ResourceId'},
        'sort': {'key': 'sort', 'type': 'str'},
        'life_time': {'key': 'lifeTime', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'unit_schema': {'key': 'unitSchema', 'type': 'str'},
        '_links': {'key': '_links', 'type': '[Link]'},
    }

    def __init__(self, href=None, key=None, value_type=None, value_required=None, display_name=None, data_format_id=None, sort=None, life_time=None, type=None, unit_schema=None, _links=None):
        super(PropertyDefinitionDto, self).__init__()
        self.href = href
        self.key = key
        self.value_type = value_type
        self.value_required = value_required
        self.display_name = display_name
        self.data_format_id = data_format_id
        self.sort = sort
        self.life_time = life_time
        self.type = type
        self.unit_schema = unit_schema
        self._links = _links
