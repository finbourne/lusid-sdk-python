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


class AnalyticsItemDto(Model):
    """AnalyticsItemDto.

    :param label:
    :type label: str
    :param security_uid:
    :type security_uid: str
    :param analytic_date:
    :type analytic_date: datetime
    :param recipe_scope:
    :type recipe_scope: str
    :param recipe_key:
    :type recipe_key: str
    :param metric_key:
    :type metric_key: dict[str, object]
    :param value:
    :type value: dict[str, object]
    """

    _validation = {
        'label': {'required': True},
        'recipe_key': {'required': True},
        'metric_key': {'required': True},
        'value': {'required': True},
    }

    _attribute_map = {
        'label': {'key': 'label', 'type': 'str'},
        'security_uid': {'key': 'securityUid', 'type': 'str'},
        'analytic_date': {'key': 'analyticDate', 'type': 'iso-8601'},
        'recipe_scope': {'key': 'recipeScope', 'type': 'str'},
        'recipe_key': {'key': 'recipeKey', 'type': 'str'},
        'metric_key': {'key': 'metricKey', 'type': '{object}'},
        'value': {'key': 'value', 'type': '{object}'},
    }

    def __init__(self, label, recipe_key, metric_key, value, security_uid=None, analytic_date=None, recipe_scope=None):
        super(AnalyticsItemDto, self).__init__()
        self.label = label
        self.security_uid = security_uid
        self.analytic_date = analytic_date
        self.recipe_scope = recipe_scope
        self.recipe_key = recipe_key
        self.metric_key = metric_key
        self.value = value
