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


class CreatePortfolioRequest(Model):
    """CreatePortfolioRequest.

    :param name:
    :type name: str
    :param code:
    :type code: str
    :param created:
    :type created: datetime
    :param base_currency:
    :type base_currency: str
    :param corporate_action_source_id:
    :type corporate_action_source_id: ~lusid.models.ResourceId
    """

    _validation = {
        'name': {'required': True},
        'code': {'required': True},
        'base_currency': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'code': {'key': 'code', 'type': 'str'},
        'created': {'key': 'created', 'type': 'iso-8601'},
        'base_currency': {'key': 'baseCurrency', 'type': 'str'},
        'corporate_action_source_id': {'key': 'corporateActionSourceId', 'type': 'ResourceId'},
    }

    def __init__(self, name, code, base_currency, created=None, corporate_action_source_id=None):
        super(CreatePortfolioRequest, self).__init__()
        self.name = name
        self.code = code
        self.created = created
        self.base_currency = base_currency
        self.corporate_action_source_id = corporate_action_source_id
