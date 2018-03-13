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


class PersonalisationDto(Model):
    """PersonalisationDto.

    :param scope: Possible values include: 'User', 'Group', 'Default', 'All'
    :type scope: str or ~lusid.models.enum
    :param scope_value:
    :type scope_value: str
    :param setting_key:
    :type setting_key: str
    :param setting_value:
    :type setting_value: str
    :param data_type:
    :type data_type: str
    :param href:
    :type href: str
    """

    _attribute_map = {
        'scope': {'key': 'scope', 'type': 'str'},
        'scope_value': {'key': 'scopeValue', 'type': 'str'},
        'setting_key': {'key': 'settingKey', 'type': 'str'},
        'setting_value': {'key': 'settingValue', 'type': 'str'},
        'data_type': {'key': 'dataType', 'type': 'str'},
        'href': {'key': 'href', 'type': 'str'},
    }

    def __init__(self, scope=None, scope_value=None, setting_key=None, setting_value=None, data_type=None, href=None):
        super(PersonalisationDto, self).__init__()
        self.scope = scope
        self.scope_value = scope_value
        self.setting_key = setting_key
        self.setting_value = setting_value
        self.data_type = data_type
        self.href = href
