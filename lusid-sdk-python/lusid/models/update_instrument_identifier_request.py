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


class UpdateInstrumentIdentifierRequest(Model):
    """UpdateInstrumentIdentifierRequest.

    :param type: The type of the identifier to upsert. This must be one of the
     code types marked as
     allowable for instrument identifiers. Possible values include:
     'Undefined', 'LusidInstrumentId', 'ReutersAssetId', 'CINS', 'Isin',
     'Sedol', 'Cusip', 'Ticker', 'ClientInternal', 'Figi', 'CompositeFigi',
     'ShareClassFigi', 'Wertpapier', 'RIC', 'QuotePermId'
    :type type: str or ~lusid.models.enum
    :param value: The value of the identifier. If set to `null`, this will
     remove the identifier completely.
     Note that, if an instrument only has one identifier, it is an error to
     remove this.
    :type value: str
    :param effective_from: The date at which the identifier modification is to
     be effective from. If unset, will
     default to `now`.
    :type effective_from: datetime
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
        'effective_from': {'key': 'effectiveFrom', 'type': 'iso-8601'},
    }

    def __init__(self, type=None, value=None, effective_from=None):
        super(UpdateInstrumentIdentifierRequest, self).__init__()
        self.type = type
        self.value = value
        self.effective_from = effective_from
