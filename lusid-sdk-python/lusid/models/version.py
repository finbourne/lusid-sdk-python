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


class Version(Model):
    """Describes the version metadata of an entity.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar effective_from:
    :vartype effective_from: datetime
    :ivar as_at_date:
    :vartype as_at_date: datetime
    :ivar href:
    :vartype href: str
    """

    _validation = {
        'effective_from': {'readonly': True},
        'as_at_date': {'readonly': True},
        'href': {'readonly': True},
    }

    _attribute_map = {
        'effective_from': {'key': 'effectiveFrom', 'type': 'iso-8601'},
        'as_at_date': {'key': 'asAtDate', 'type': 'iso-8601'},
        'href': {'key': 'href', 'type': 'str'},
    }

    def __init__(self):
        super(Version, self).__init__()
        self.effective_from = None
        self.as_at_date = None
        self.href = None
