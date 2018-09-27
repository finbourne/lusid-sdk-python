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


class HoldingsAdjustmentHeader(Model):
    """Summary information of a holdings adjustment for a single portfolio and
    effective date.

    :param effective_at: There can be at most one holdings adjustment for a
     portfolio at a
     specific effective time so this uniquely identifies the adjustment.
    :type effective_at: datetime
    :param version:
    :type version: ~lusid.models.Version
    :param unmatched_holding_method: Possible values include:
     'PositionToZero', 'KeepTheSame'
    :type unmatched_holding_method: str or ~lusid.models.enum
    :param links:
    :type links: list[~lusid.models.Link]
    """

    _attribute_map = {
        'effective_at': {'key': 'effectiveAt', 'type': 'iso-8601'},
        'version': {'key': 'version', 'type': 'Version'},
        'unmatched_holding_method': {'key': 'unmatchedHoldingMethod', 'type': 'str'},
        'links': {'key': 'links', 'type': '[Link]'},
    }

    def __init__(self, effective_at=None, version=None, unmatched_holding_method=None, links=None):
        super(HoldingsAdjustmentHeader, self).__init__()
        self.effective_at = effective_at
        self.version = version
        self.unmatched_holding_method = unmatched_holding_method
        self.links = links
