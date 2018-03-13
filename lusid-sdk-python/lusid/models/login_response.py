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


class LoginResponse(Model):
    """LoginResponse.

    :param name:
    :type name: str
    :param first_name:
    :type first_name: str
    :param default_scope:
    :type default_scope: str
    :param session_context_id:
    :type session_context_id: str
    :param logo_uri:
    :type logo_uri: str
    :param value_currency_code:
    :type value_currency_code: str
    :param value_currency_symbol:
    :type value_currency_symbol: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'first_name': {'key': 'firstName', 'type': 'str'},
        'default_scope': {'key': 'defaultScope', 'type': 'str'},
        'session_context_id': {'key': 'sessionContextId', 'type': 'str'},
        'logo_uri': {'key': 'logoUri', 'type': 'str'},
        'value_currency_code': {'key': 'valueCurrencyCode', 'type': 'str'},
        'value_currency_symbol': {'key': 'valueCurrencySymbol', 'type': 'str'},
    }

    def __init__(self, name=None, first_name=None, default_scope=None, session_context_id=None, logo_uri=None, value_currency_code=None, value_currency_symbol=None):
        super(LoginResponse, self).__init__()
        self.name = name
        self.first_name = first_name
        self.default_scope = default_scope
        self.session_context_id = session_context_id
        self.logo_uri = logo_uri
        self.value_currency_code = value_currency_code
        self.value_currency_symbol = value_currency_symbol
