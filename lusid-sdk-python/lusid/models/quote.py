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


class Quote(Model):
    """Quote.

    :param quote_id:
    :type quote_id: ~lusid.models.QuoteId
    :param metric_value:
    :type metric_value: ~lusid.models.MetricValue
    :param effective_at_date:
    :type effective_at_date: datetime
    :param as_at_date:
    :type as_at_date: datetime
    """

    _validation = {
        'quote_id': {'required': True},
        'metric_value': {'required': True},
    }

    _attribute_map = {
        'quote_id': {'key': 'quoteId', 'type': 'QuoteId'},
        'metric_value': {'key': 'metricValue', 'type': 'MetricValue'},
        'effective_at_date': {'key': 'effectiveAtDate', 'type': 'iso-8601'},
        'as_at_date': {'key': 'asAtDate', 'type': 'iso-8601'},
    }

    def __init__(self, quote_id, metric_value, effective_at_date=None, as_at_date=None):
        super(Quote, self).__init__()
        self.quote_id = quote_id
        self.metric_value = metric_value
        self.effective_at_date = effective_at_date
        self.as_at_date = as_at_date
