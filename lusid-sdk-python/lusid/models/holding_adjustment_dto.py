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


class HoldingAdjustmentDto(Model):
    """Used to specify the 'target' holding when calling the AdjustHoldings Api.

    :param href:
    :type href: str
    :param security_uid:
    :type security_uid: str
    :param units:
    :type units: float
    :param cost:
    :type cost: float
    :param properties:
    :type properties: list[~lusid.models.PropertyDto]
    :param _links:
    :type _links: list[~lusid.models.Link]
    """

    _attribute_map = {
        'href': {'key': 'href', 'type': 'str'},
        'security_uid': {'key': 'securityUid', 'type': 'str'},
        'units': {'key': 'units', 'type': 'float'},
        'cost': {'key': 'cost', 'type': 'float'},
        'properties': {'key': 'properties', 'type': '[PropertyDto]'},
        '_links': {'key': '_links', 'type': '[Link]'},
    }

    def __init__(self, href=None, security_uid=None, units=None, cost=None, properties=None, _links=None):
        super(HoldingAdjustmentDto, self).__init__()
        self.href = href
        self.security_uid = security_uid
        self.units = units
        self.cost = cost
        self.properties = properties
        self._links = _links
