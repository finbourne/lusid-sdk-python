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


class AggregationOptions(Model):
    """Options for controlling the default aspects and behaviour of the
    aggregation.

    :param use_ansi_like_syntax: Should the aggregation behave like ANSI Sql
     or MySql with respect to a conceptual request which is equivalent to
     "select a,sum(a) from results";
     ANSI Sql would report an error if a was not unique where MySql would
     simply view a,suma(a) as equivalent to firstof(a),sum(a).
    :type use_ansi_like_syntax: bool
    """

    _attribute_map = {
        'use_ansi_like_syntax': {'key': 'useAnsiLikeSyntax', 'type': 'bool'},
    }

    def __init__(self, use_ansi_like_syntax=None):
        super(AggregationOptions, self).__init__()
        self.use_ansi_like_syntax = use_ansi_like_syntax
