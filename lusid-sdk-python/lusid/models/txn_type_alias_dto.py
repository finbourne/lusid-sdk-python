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


class TxnTypeAliasDto(Model):
    """TxnTypeAliasDto.

    :param type: The transaction type
    :type type: str
    :param description: Brief description of the transaction
    :type description: str
    :param txn_class: Relates types of a similar class. E.g. Buy/Sell,
     StockIn/StockOut
    :type txn_class: str
    :param txn_group: Group is a set of codes related to a source, or sync
    :type txn_group: str
    :param txn_roles: Transactions role within a class. E.g. Increase a long
     position. Possible values include: 'None', 'LongLonger', 'LongShorter',
     'ShortShorter', 'ShortLonger', 'Longer', 'Shorter', 'AllRoles'
    :type txn_roles: str or ~lusid.models.enum
    """

    _validation = {
        'type': {'required': True},
        'description': {'required': True},
        'txn_class': {'required': True},
        'txn_group': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'txn_class': {'key': 'txnClass', 'type': 'str'},
        'txn_group': {'key': 'txnGroup', 'type': 'str'},
        'txn_roles': {'key': 'txnRoles', 'type': 'str'},
    }

    def __init__(self, type, description, txn_class, txn_group, txn_roles=None):
        super(TxnTypeAliasDto, self).__init__()
        self.type = type
        self.description = description
        self.txn_class = txn_class
        self.txn_group = txn_group
        self.txn_roles = txn_roles
