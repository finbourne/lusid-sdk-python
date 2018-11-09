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


class VersionSummaryDto(Model):
    """VersionSummaryDto.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar api_version:
    :vartype api_version: str
    :ivar build_version:
    :vartype build_version: str
    :ivar excel_version:
    :vartype excel_version: str
    :param links:
    :type links: list[~lusid.models.Link]
    """

    _validation = {
        'api_version': {'readonly': True},
        'build_version': {'readonly': True},
        'excel_version': {'readonly': True},
    }

    _attribute_map = {
        'api_version': {'key': 'apiVersion', 'type': 'str'},
        'build_version': {'key': 'buildVersion', 'type': 'str'},
        'excel_version': {'key': 'excelVersion', 'type': 'str'},
        'links': {'key': 'links', 'type': '[Link]'},
    }

    def __init__(self, links=None):
        super(VersionSummaryDto, self).__init__()
        self.api_version = None
        self.build_version = None
        self.excel_version = None
        self.links = links
