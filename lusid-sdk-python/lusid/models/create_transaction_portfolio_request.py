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


class CreateTransactionPortfolioRequest(Model):
    """CreateTransactionPortfolioRequest.

    :param display_name:
    :type display_name: str
    :param description:
    :type description: str
    :param code:
    :type code: str
    :param created:
    :type created: datetime
    :param base_currency:
    :type base_currency: str
    :param corporate_action_source_id:
    :type corporate_action_source_id: ~lusid.models.ResourceId
    :param accounting_method: Possible values include: 'Default',
     'AverageCost', 'FirstInFirstOut', 'LastInFirstOut', 'HighestCostFirst',
     'LowestCostFirst'
    :type accounting_method: str or ~lusid.models.enum
    :param sub_holding_keys:
    :type sub_holding_keys: list[str]
    :param properties: Portfolio properties to add to the portfolio
    :type properties: dict[str, ~lusid.models.PropertyValue]
    """

    _validation = {
        'display_name': {'required': True},
        'code': {'required': True},
        'base_currency': {'required': True},
    }

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'code': {'key': 'code', 'type': 'str'},
        'created': {'key': 'created', 'type': 'iso-8601'},
        'base_currency': {'key': 'baseCurrency', 'type': 'str'},
        'corporate_action_source_id': {'key': 'corporateActionSourceId', 'type': 'ResourceId'},
        'accounting_method': {'key': 'accountingMethod', 'type': 'str'},
        'sub_holding_keys': {'key': 'subHoldingKeys', 'type': '[str]'},
        'properties': {'key': 'properties', 'type': '{PropertyValue}'},
    }

    def __init__(self, display_name, code, base_currency, description=None, created=None, corporate_action_source_id=None, accounting_method=None, sub_holding_keys=None, properties=None):
        super(CreateTransactionPortfolioRequest, self).__init__()
        self.display_name = display_name
        self.description = description
        self.code = code
        self.created = created
        self.base_currency = base_currency
        self.corporate_action_source_id = corporate_action_source_id
        self.accounting_method = accounting_method
        self.sub_holding_keys = sub_holding_keys
        self.properties = properties
