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


class IUnitDefinition(Model):
    """IUnitDefinition.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar schema: Possible values include: 'NoUnits', 'Basic',
     'Iso4217Currency'
    :vartype schema: str or ~lusid.models.enum
    :ivar code:
    :vartype code: str
    :ivar display_name:
    :vartype display_name: str
    :ivar description:
    :vartype description: str
    """

    _validation = {
        'schema': {'readonly': True},
        'code': {'readonly': True},
        'display_name': {'readonly': True},
        'description': {'readonly': True},
    }

    _attribute_map = {
        'schema': {'key': 'schema', 'type': 'str'},
        'code': {'key': 'code', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self):
        super(IUnitDefinition, self).__init__()
        self.schema = None
        self.code = None
        self.display_name = None
        self.description = None
