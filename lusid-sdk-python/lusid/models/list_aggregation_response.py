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


class ListAggregationResponse(Model):
    """ListAggregationResponse.

    :param href:
    :type href: str
    :param data:
    :type data: list[dict[str, object]]
    :param aggregation_currency:
    :type aggregation_currency: str
    :param data_schema:
    :type data_schema: ~lusid.models.ResultDataSchema
    :param links:
    :type links: list[~lusid.models.Link]
    """

    _attribute_map = {
        'href': {'key': 'href', 'type': 'str'},
        'data': {'key': 'data', 'type': '[{object}]'},
        'aggregation_currency': {'key': 'aggregationCurrency', 'type': 'str'},
        'data_schema': {'key': 'dataSchema', 'type': 'ResultDataSchema'},
        'links': {'key': 'links', 'type': '[Link]'},
    }

    def __init__(self, href=None, data=None, aggregation_currency=None, data_schema=None, links=None):
        super(ListAggregationResponse, self).__init__()
        self.href = href
        self.data = data
        self.aggregation_currency = aggregation_currency
        self.data_schema = data_schema
        self.links = links
