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


class CreateReferencePortfolioRequest(Model):
    """CreateReferencePortfolioRequest.

    :param display_name:
    :type display_name: str
    :param description:
    :type description: str
    :param code:
    :type code: str
    :param created:
    :type created: datetime
    :param properties: Portfolio properties to add to the portfolio
    :type properties: dict[str, ~lusid.models.PerpetualPropertyValue]
    """

    _validation = {
        'display_name': {'required': True},
        'code': {'required': True},
    }

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'code': {'key': 'code', 'type': 'str'},
        'created': {'key': 'created', 'type': 'iso-8601'},
        'properties': {'key': 'properties', 'type': '{PerpetualPropertyValue}'},
    }

    def __init__(self, display_name, code, description=None, created=None, properties=None):
        super(CreateReferencePortfolioRequest, self).__init__()
        self.display_name = display_name
        self.description = description
        self.code = code
        self.created = created
        self.properties = properties
