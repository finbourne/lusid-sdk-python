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


class TransactionQueryParameters(Model):
    """TransactionQueryParameters.

    :param start_date: The required set of transactions should begin from this
     date
    :type start_date: datetime
    :param end_date: The required set of transactions should end at this date
    :type end_date: datetime
    :param query_mode: The method for date selection. Trade date or Settlement
     date. Possible values include: 'None', 'TradeDate', 'SettleDate'
    :type query_mode: str or ~lusid.models.enum
    :param show_cancelled_transactions: Option to include cancelled
     transactions in the results
    :type show_cancelled_transactions: bool
    """

    _attribute_map = {
        'start_date': {'key': 'startDate', 'type': 'iso-8601'},
        'end_date': {'key': 'endDate', 'type': 'iso-8601'},
        'query_mode': {'key': 'queryMode', 'type': 'str'},
        'show_cancelled_transactions': {'key': 'showCancelledTransactions', 'type': 'bool'},
    }

    def __init__(self, start_date=None, end_date=None, query_mode=None, show_cancelled_transactions=None):
        super(TransactionQueryParameters, self).__init__()
        self.start_date = start_date
        self.end_date = end_date
        self.query_mode = query_mode
        self.show_cancelled_transactions = show_cancelled_transactions
