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


class InstrumentMatch(Model):
    """InstrumentMatch.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name:
    :vartype name: str
    :ivar aliases:
    :vartype aliases: ~lusid.models.InstrumentMatchAliases
    :ivar bloomberg_exchange_code:
    :vartype bloomberg_exchange_code: str
    :ivar market_identifier_code:
    :vartype market_identifier_code: str
    """

    _validation = {
        'name': {'readonly': True},
        'aliases': {'readonly': True},
        'bloomberg_exchange_code': {'readonly': True},
        'market_identifier_code': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'aliases': {'key': 'aliases', 'type': 'InstrumentMatchAliases'},
        'bloomberg_exchange_code': {'key': 'bloombergExchangeCode', 'type': 'str'},
        'market_identifier_code': {'key': 'marketIdentifierCode', 'type': 'str'},
    }

    def __init__(self):
        super(InstrumentMatch, self).__init__()
        self.name = None
        self.aliases = None
        self.bloomberg_exchange_code = None
        self.market_identifier_code = None
