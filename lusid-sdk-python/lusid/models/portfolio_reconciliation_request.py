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


class PortfolioReconciliationRequest(Model):
    """PortfolioReconciliationRequest.

    :param portfolio_id: The id of the portfolio to be reconciled
    :type portfolio_id: ~lusid.models.ResourceId
    :param effective_at: The effective date of the portfolio
    :type effective_at: datetime
    :param as_at: Optional. The AsAt date of the portfolio
    :type as_at: datetime
    """

    _validation = {
        'portfolio_id': {'required': True},
        'effective_at': {'required': True},
    }

    _attribute_map = {
        'portfolio_id': {'key': 'portfolioId', 'type': 'ResourceId'},
        'effective_at': {'key': 'effectiveAt', 'type': 'iso-8601'},
        'as_at': {'key': 'asAt', 'type': 'iso-8601'},
    }

    def __init__(self, portfolio_id, effective_at, as_at=None):
        super(PortfolioReconciliationRequest, self).__init__()
        self.portfolio_id = portfolio_id
        self.effective_at = effective_at
        self.as_at = as_at
