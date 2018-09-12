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


class AggregationResponseNodeOfDictionaryOfStringToObject(Model):
    """AggregationResponseNodeOfDictionaryOfStringToObject.

    :param group_property_key:
    :type group_property_key: str
    :param group_property_value:
    :type group_property_value: str
    :param idx:
    :type idx: int
    :param properties:
    :type properties: dict[str, object]
    :param children:
    :type children:
     list[~lusid.models.AggregationResponseNodeOfDictionaryOfStringToObject]
    """

    _attribute_map = {
        'group_property_key': {'key': 'groupPropertyKey', 'type': 'str'},
        'group_property_value': {'key': 'groupPropertyValue', 'type': 'str'},
        'idx': {'key': 'idx', 'type': 'int'},
        'properties': {'key': 'properties', 'type': '{object}'},
        'children': {'key': 'children', 'type': '[AggregationResponseNodeOfDictionaryOfStringToObject]'},
    }

    def __init__(self, group_property_key=None, group_property_value=None, idx=None, properties=None, children=None):
        super(AggregationResponseNodeOfDictionaryOfStringToObject, self).__init__()
        self.group_property_key = group_property_key
        self.group_property_value = group_property_value
        self.idx = idx
        self.properties = properties
        self.children = children
