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

    :param security_uid:
    :type security_uid: str
    :param properties:
    :type properties: list[~lusid.models.PropertyDto]
    :param holding_type:
    :type holding_type: str
    :param units:
    :type units: float
    :param settled_units:
    :type settled_units: float
    :param cost:
    :type cost: float
    :param transaction:
    :type transaction: ~lusid.models.TradeDto
    """

    _validation = {
        'security_uid': {'required': True},
        'holding_type': {'required': True},
        'units': {'required': True},
        'settled_units': {'required': True},
        'cost': {'required': True},
    }

    _attribute_map = {
        'security_uid': {'key': 'securityUid', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '[PropertyDto]'},
        'holding_type': {'key': 'holdingType', 'type': 'str'},
        'units': {'key': 'units', 'type': 'float'},
        'settled_units': {'key': 'settledUnits', 'type': 'float'},
        'cost': {'key': 'cost', 'type': 'float'},
        'transaction': {'key': 'transaction', 'type': 'TradeDto'},
    }

    def __init__(self, security_uid, holding_type, units, settled_units, cost, properties=None, transaction=None):
        super(HoldingDto, self).__init__()
        self.security_uid = security_uid
        self.properties = properties
        self.holding_type = holding_type
        self.units = units
        self.settled_units = settled_units
        self.cost = cost
        self.transaction = transaction
