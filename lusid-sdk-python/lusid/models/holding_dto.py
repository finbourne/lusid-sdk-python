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


class HoldingDto(Model):
    """HoldingDto.

    :param security_uid: Unique security identifier
    :type security_uid: str
    :param properties:
    :type properties: list[~lusid.models.PropertyDto]
    :param holding_type: Type of holding, eg Position, Balance,
     CashCommitment, Receivable, ForwardFX
    :type holding_type: str
    :param units: Quantity of holding
    :type units: float
    :param settled_units: Settled quantity of holding
    :type settled_units: float
    :param cost: Book cost of holding in trade currency
    :type cost: float
    :param cost_portfolio_ccy: Book cost of holding in portfolio currency
    :type cost_portfolio_ccy: float
    :param transaction: If this is commitment-type holding, the transaction
     behind it
    :type transaction: ~lusid.models.TradeDto
    """

    _validation = {
        'holding_type': {'required': True},
    }

    _attribute_map = {
        'security_uid': {'key': 'securityUid', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '[PropertyDto]'},
        'holding_type': {'key': 'holdingType', 'type': 'str'},
        'units': {'key': 'units', 'type': 'float'},
        'settled_units': {'key': 'settledUnits', 'type': 'float'},
        'cost': {'key': 'cost', 'type': 'float'},
        'cost_portfolio_ccy': {'key': 'costPortfolioCcy', 'type': 'float'},
        'transaction': {'key': 'transaction', 'type': 'TradeDto'},
    }

    def __init__(self, holding_type, security_uid=None, properties=None, units=None, settled_units=None, cost=None, cost_portfolio_ccy=None, transaction=None):
        super(HoldingDto, self).__init__()
        self.security_uid = security_uid
        self.properties = properties
        self.holding_type = holding_type
        self.units = units
        self.settled_units = settled_units
        self.cost = cost
        self.cost_portfolio_ccy = cost_portfolio_ccy
        self.transaction = transaction
