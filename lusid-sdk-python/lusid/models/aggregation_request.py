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

    :param recipe_id: The configuration recipe, consisting of user scope and
     recipe name, to use in performing the aggregation.
    :type recipe_id: ~lusid.models.ResourceId
    :param as_at: The asAt date to use
    :type as_at: datetime
    :param effective_at: The market data time, i.e. the time to run the
     aggregation request effective of.
    :type effective_at: datetime
    :param metrics: The set of specifications for items to calculate or
     retrieve during the aggregation and present in the results.
     This is logically equivalent to the set of operations in a Sql select
     statement
     select [operation1(field1), operation2(field2), ... ] from results
    :type metrics: list[~lusid.models.AggregateSpec]
    :param group_by: The set of items by which to perform grouping. This
     primarily matters when one or more of the metric operators is a mapping
     that reduces set size, e.g. sum or proportion. The group-by statement
     determines the set of keys by which to break the results out.
    :type group_by: list[str]
    :param filters: A set of filters to use to reduce the data found in a
     request. Equivalent to the 'where ...' part of a Sql select statement.
     For example, filter a set of values within a given range or matching a
     particular value.
    :type filters: list[~lusid.models.PropertyFilter]
    :param limit: limit the results to a particular number of values.
    :type limit: int
    :param sort: Sort the results or not.
    :type sort: str
    """

    _validation = {
        'recipe_id': {'required': True},
        'effective_at': {'required': True},
        'metrics': {'required': True},
    }

    _attribute_map = {
        'recipe_id': {'key': 'recipeId', 'type': 'ResourceId'},
        'as_at': {'key': 'asAt', 'type': 'iso-8601'},
        'effective_at': {'key': 'effectiveAt', 'type': 'iso-8601'},
        'metrics': {'key': 'metrics', 'type': '[AggregateSpec]'},
        'group_by': {'key': 'groupBy', 'type': '[str]'},
        'filters': {'key': 'filters', 'type': '[PropertyFilter]'},
        'limit': {'key': 'limit', 'type': 'int'},
        'sort': {'key': 'sort', 'type': 'str'},
    }

    def __init__(self, recipe_id, effective_at, metrics, as_at=None, group_by=None, filters=None, limit=None, sort=None):
        super(AggregationRequest, self).__init__()
        self.recipe_id = recipe_id
        self.as_at = as_at
        self.effective_at = effective_at
        self.metrics = metrics
        self.group_by = group_by
        self.filters = filters
        self.limit = limit
        self.sort = sort
