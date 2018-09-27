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


class CreatePortfolioGroupRequest(Model):
    """CreatePortfolioGroupRequest.

    :param id:
    :type id: str
    :param values:
    :type values: list[~lusid.models.ResourceId]
    :param sub_groups:
    :type sub_groups: list[~lusid.models.ResourceId]
    :param display_name:
    :type display_name: str
    :param description:
    :type description: str
    """

    _validation = {
        'id': {'required': True},
        'display_name': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'values': {'key': 'values', 'type': '[ResourceId]'},
        'sub_groups': {'key': 'subGroups', 'type': '[ResourceId]'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, id, display_name, values=None, sub_groups=None, description=None):
        super(CreatePortfolioGroupRequest, self).__init__()
        self.id = id
        self.values = values
        self.sub_groups = sub_groups
        self.display_name = display_name
        self.description = description
