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


class ExecutionRequest(Model):
    """ExecutionRequest.

    :param execution_id: FIX Field 17.  Unique execution identifier.
    :type execution_id: str
    :param side: FIX Field 54.
    :type side: str
    :param instrument_uid: Unique instrument identifier.
    :type instrument_uid: str
    :param transaction_time: FIX field 60.  Time the transaction represented
     by this ExecutionReport occurred.
    :type transaction_time: datetime
    :param order_qty: FIX field 38.  Order quantity.
    :type order_qty: float
    :param price: FIX field 44.
    :type price: float
    :param currency: FIX field 15.
    :type currency: str
    """

    _validation = {
        'execution_id': {'required': True},
        'side': {'required': True},
        'instrument_uid': {'required': True},
        'transaction_time': {'required': True},
        'order_qty': {'required': True},
        'price': {'required': True},
        'currency': {'required': True},
    }

    _attribute_map = {
        'execution_id': {'key': 'executionId', 'type': 'str'},
        'side': {'key': 'side', 'type': 'str'},
        'instrument_uid': {'key': 'instrumentUid', 'type': 'str'},
        'transaction_time': {'key': 'transactionTime', 'type': 'iso-8601'},
        'order_qty': {'key': 'orderQty', 'type': 'float'},
        'price': {'key': 'price', 'type': 'float'},
        'currency': {'key': 'currency', 'type': 'str'},
    }

    def __init__(self, execution_id, side, instrument_uid, transaction_time, order_qty, price, currency):
        super(ExecutionRequest, self).__init__()
        self.execution_id = execution_id
        self.side = side
        self.instrument_uid = instrument_uid
        self.transaction_time = transaction_time
        self.order_qty = order_qty
        self.price = price
        self.currency = currency
