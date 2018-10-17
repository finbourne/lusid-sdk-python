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


class ReconciliationBreak(Model):
    """A reconciliation break.

    :param instrument_uid: Unique instrument identifier
    :type instrument_uid: str
    :param sub_holding_keys: Any other properties that comprise the
     Sub-Holding Key
    :type sub_holding_keys: list[~lusid.models.Property]
    :param left_units: Units from the left hand side
    :type left_units: float
    :param right_units: Units from the right hand side
    :type right_units: float
    :param difference_units: Difference in units
    :type difference_units: float
    :param left_cost: Cost from the left hand side
    :type left_cost: ~lusid.models.CurrencyAndAmount
    :param right_cost: Cost from the right hand side
    :type right_cost: ~lusid.models.CurrencyAndAmount
    :param difference_cost: Difference in cost
    :type difference_cost: ~lusid.models.CurrencyAndAmount
    :param instrument_properties: Additional features relating to the security
    :type instrument_properties: list[~lusid.models.Property]
    """

    _validation = {
        'instrument_uid': {'required': True},
        'sub_holding_keys': {'required': True},
        'left_units': {'required': True},
        'right_units': {'required': True},
        'difference_units': {'required': True},
        'left_cost': {'required': True},
        'right_cost': {'required': True},
        'difference_cost': {'required': True},
        'instrument_properties': {'required': True},
    }

    _attribute_map = {
        'instrument_uid': {'key': 'instrumentUid', 'type': 'str'},
        'sub_holding_keys': {'key': 'subHoldingKeys', 'type': '[Property]'},
        'left_units': {'key': 'leftUnits', 'type': 'float'},
        'right_units': {'key': 'rightUnits', 'type': 'float'},
        'difference_units': {'key': 'differenceUnits', 'type': 'float'},
        'left_cost': {'key': 'leftCost', 'type': 'CurrencyAndAmount'},
        'right_cost': {'key': 'rightCost', 'type': 'CurrencyAndAmount'},
        'difference_cost': {'key': 'differenceCost', 'type': 'CurrencyAndAmount'},
        'instrument_properties': {'key': 'instrumentProperties', 'type': '[Property]'},
    }

    def __init__(self, instrument_uid, sub_holding_keys, left_units, right_units, difference_units, left_cost, right_cost, difference_cost, instrument_properties):
        super(ReconciliationBreak, self).__init__()
        self.instrument_uid = instrument_uid
        self.sub_holding_keys = sub_holding_keys
        self.left_units = left_units
        self.right_units = right_units
        self.difference_units = difference_units
        self.left_cost = left_cost
        self.right_cost = right_cost
        self.difference_cost = difference_cost
        self.instrument_properties = instrument_properties
