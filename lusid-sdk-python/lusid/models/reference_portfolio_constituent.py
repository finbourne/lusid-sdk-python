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


class ReferencePortfolioConstituent(Model):
    """ReferencePortfolioConstituent.

    :param instrument_uid:
    :type instrument_uid: str
    :param currency:
    :type currency: str
    :param properties: Properties associated with the constituent
    :type properties: list[~lusid.models.Property]
    :param weight:
    :type weight: float
    :param floating_weight:
    :type floating_weight: float
    """

    _validation = {
        'instrument_uid': {'required': True},
        'currency': {'required': True},
        'weight': {'required': True},
    }

    _attribute_map = {
        'instrument_uid': {'key': 'instrumentUid', 'type': 'str'},
        'currency': {'key': 'currency', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '[Property]'},
        'weight': {'key': 'weight', 'type': 'float'},
        'floating_weight': {'key': 'floatingWeight', 'type': 'float'},
    }

    def __init__(self, instrument_uid, currency, weight, properties=None, floating_weight=None):
        super(ReferencePortfolioConstituent, self).__init__()
        self.instrument_uid = instrument_uid
        self.currency = currency
        self.properties = properties
        self.weight = weight
        self.floating_weight = floating_weight
