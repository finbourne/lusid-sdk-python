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


class UpdatePropertyDefinitionRequest(Model):
    """UpdatePropertyDefinitionRequest.

    :param value_required:
    :type value_required: bool
    :param display_name:
    :type display_name: str
    :param data_type_id:
    :type data_type_id: ~lusid.models.ResourceId
    :param life_time: Possible values include: 'Perpetual', 'TimeVariant'
    :type life_time: str or ~lusid.models.enum
    :param type: Possible values include: 'Label', 'Metric'
    :type type: str or ~lusid.models.enum
    """

    _attribute_map = {
        'value_required': {'key': 'valueRequired', 'type': 'bool'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'data_type_id': {'key': 'dataTypeId', 'type': 'ResourceId'},
        'life_time': {'key': 'lifeTime', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, value_required=None, display_name=None, data_type_id=None, life_time=None, type=None):
        super(UpdatePropertyDefinitionRequest, self).__init__()
        self.value_required = value_required
        self.display_name = display_name
        self.data_type_id = data_type_id
        self.life_time = life_time
        self.type = type
