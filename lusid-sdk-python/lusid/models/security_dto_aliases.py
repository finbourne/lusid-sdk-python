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


class SecurityDtoAliases(Model):
    """SecurityDtoAliases.

    :param undefined:
    :type undefined: str
    :param reuters_asset_id:
    :type reuters_asset_id: str
    :param cins:
    :type cins: str
    :param isin:
    :type isin: str
    :param sedol:
    :type sedol: str
    :param cusip:
    :type cusip: str
    :param client_internal:
    :type client_internal: str
    :param figi:
    :type figi: str
    :param wertpapier:
    :type wertpapier: str
    """

    _attribute_map = {
        'undefined': {'key': 'Undefined', 'type': 'str'},
        'reuters_asset_id': {'key': 'ReutersAssetId', 'type': 'str'},
        'cins': {'key': 'CINS', 'type': 'str'},
        'isin': {'key': 'Isin', 'type': 'str'},
        'sedol': {'key': 'Sedol', 'type': 'str'},
        'cusip': {'key': 'Cusip', 'type': 'str'},
        'client_internal': {'key': 'ClientInternal', 'type': 'str'},
        'figi': {'key': 'Figi', 'type': 'str'},
        'wertpapier': {'key': 'Wertpapier', 'type': 'str'},
    }

    def __init__(self, undefined=None, reuters_asset_id=None, cins=None, isin=None, sedol=None, cusip=None, client_internal=None, figi=None, wertpapier=None):
        super(SecurityDtoAliases, self).__init__()
        self.undefined = undefined
        self.reuters_asset_id = reuters_asset_id
        self.cins = cins
        self.isin = isin
        self.sedol = sedol
        self.cusip = cusip
        self.client_internal = client_internal
        self.figi = figi
        self.wertpapier = wertpapier
