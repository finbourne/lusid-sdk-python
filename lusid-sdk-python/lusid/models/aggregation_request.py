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


class AggregationRequest(Model):
    """Specification object for the parameters of an aggregation.

    :param recipe_scope:
    :type recipe_scope: str
    :param recipe_key:
    :type recipe_key: str
    :param load_reference_portfolio:
    :type load_reference_portfolio: bool
    :param as_at: The asAt date to use
    :type as_at: datetime
    :param effective_at:
    :type effective_at: datetime
    :param metrics:
    :type metrics: list[~lusid.models.AggregateSpec]
    :param group_by:
    :type group_by: list[str]
    :param filters:
    :type filters: list[~lusid.models.PropertyFilter]
    :param limit:
    :type limit: int
    :param sort:
    :type sort: str
    """

    _attribute_map = {
        'recipe_scope': {'key': 'recipeScope', 'type': 'str'},
        'recipe_key': {'key': 'recipeKey', 'type': 'str'},
        'load_reference_portfolio': {'key': 'loadReferencePortfolio', 'type': 'bool'},
        'as_at': {'key': 'asAt', 'type': 'iso-8601'},
        'effective_at': {'key': 'effectiveAt', 'type': 'iso-8601'},
        'metrics': {'key': 'metrics', 'type': '[AggregateSpec]'},
        'group_by': {'key': 'groupBy', 'type': '[str]'},
        'filters': {'key': 'filters', 'type': '[PropertyFilter]'},
        'limit': {'key': 'limit', 'type': 'int'},
        'sort': {'key': 'sort', 'type': 'str'},
    }

    def __init__(self, recipe_scope=None, recipe_key=None, load_reference_portfolio=None, as_at=None, effective_at=None, metrics=None, group_by=None, filters=None, limit=None, sort=None):
        super(AggregationRequest, self).__init__()
        self.recipe_scope = recipe_scope
        self.recipe_key = recipe_key
        self.load_reference_portfolio = load_reference_portfolio
        self.as_at = as_at
        self.effective_at = effective_at
        self.metrics = metrics
        self.group_by = group_by
        self.filters = filters
        self.limit = limit
        self.sort = sort
