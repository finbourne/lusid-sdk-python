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


class CreateResults(Model):
    """CreateResults.

    :param data:
    :type data: str
    :param scope:
    :type scope: str
    :param key: The key is a unique point in 'run' space. For a given scope
     and time point, one would wish to
     identify a unique result set for a given recipe. In essence, this key is
     the unique identifier for the tuple (recipe,portfolios)
     However, that only matters when one is trying to use it automatically to
     retrieve them.
     A question becomes whether we would wish to store groups of protfolio
     results together, or only single ones.
     Also, whether we would accept uploading of groups and then split them
     apart.
    :type key: str
    :param date_property:
    :type date_property: datetime
    :param format: Possible values include: 'DataReader', 'Portfolio'
    :type format: str or ~lusid.models.enum
    """

    _attribute_map = {
        'data': {'key': 'data', 'type': 'str'},
        'scope': {'key': 'scope', 'type': 'str'},
        'key': {'key': 'key', 'type': 'str'},
        'date_property': {'key': 'date', 'type': 'iso-8601'},
        'format': {'key': 'format', 'type': 'str'},
    }

    def __init__(self, data=None, scope=None, key=None, date_property=None, format=None):
        super(CreateResults, self).__init__()
        self.data = data
        self.scope = scope
        self.key = key
        self.date_property = date_property
        self.format = format
