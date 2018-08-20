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


class SecurityDto(Model):
    """SecurityDto.

    :param href:
    :type href: str
    :param uid:
    :type uid: str
    :param version:
    :type version: ~lusid.models.VersionDto
    :param common_name:
    :type common_name: str
    :param aliases:
    :type aliases: dict[str, str]
    :param properties:
    :type properties: list[~lusid.models.PropertyDto]
    :param market_identifier_code:
    :type market_identifier_code: str
    :param _links:
    :type _links: list[~lusid.models.Link]
    """

    _attribute_map = {
        'href': {'key': 'href', 'type': 'str'},
        'uid': {'key': 'uid', 'type': 'str'},
        'version': {'key': 'version', 'type': 'VersionDto'},
        'common_name': {'key': 'commonName', 'type': 'str'},
        'aliases': {'key': 'aliases', 'type': '{str}'},
        'properties': {'key': 'properties', 'type': '[PropertyDto]'},
        'market_identifier_code': {'key': 'marketIdentifierCode', 'type': 'str'},
        '_links': {'key': '_links', 'type': '[Link]'},
    }

    def __init__(self, href=None, uid=None, version=None, common_name=None, aliases=None, properties=None, market_identifier_code=None, _links=None):
        super(SecurityDto, self).__init__()
        self.href = href
        self.uid = uid
        self.version = version
        self.common_name = common_name
        self.aliases = aliases
        self.properties = properties
        self.market_identifier_code = market_identifier_code
        self._links = _links
