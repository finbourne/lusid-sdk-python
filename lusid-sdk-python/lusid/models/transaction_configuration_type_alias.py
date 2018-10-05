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


class TransactionConfigurationTypeAlias(Model):
    """TransactionConfigurationTypeAlias.

    :param type: The transaction type
    :type type: str
    :param description: Brief description of the transaction
    :type description: str
    :param transaction_class: Relates types of a similar class. E.g. Buy/Sell,
     StockIn/StockOut
    :type transaction_class: str
    :param transaction_group: Group is a set of codes related to a source, or
     sync
    :type transaction_group: str
    :param transaction_roles: Transactions role within a class. E.g. Increase
     a long position. Possible values include: 'None', 'LongLonger',
     'LongShorter', 'ShortShorter', 'ShortLonger', 'Longer', 'Shorter',
     'AllRoles'
    :type transaction_roles: str or ~lusid.models.enum
    """

    _validation = {
        'type': {'required': True},
        'description': {'required': True},
        'transaction_class': {'required': True},
        'transaction_group': {'required': True},
        'transaction_roles': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'transaction_class': {'key': 'transactionClass', 'type': 'str'},
        'transaction_group': {'key': 'transactionGroup', 'type': 'str'},
        'transaction_roles': {'key': 'transactionRoles', 'type': 'str'},
    }

    def __init__(self, type, description, transaction_class, transaction_group, transaction_roles):
        super(TransactionConfigurationTypeAlias, self).__init__()
        self.type = type
        self.description = description
        self.transaction_class = transaction_class
        self.transaction_group = transaction_group
        self.transaction_roles = transaction_roles
