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


class PropertyFilter(Model):
    """PropertyFilter.

    :param left:
    :type left: str
    :param operator: Possible values include: 'Equals', 'NotEquals',
     'GreaterThan', 'GreaterThanOrEqualTo', 'LessThan', 'LessThanOrEqualTo',
     'In'
    :type operator: str or ~lusid.models.enum
    :param right:
    :type right: object
    :param right_operand_type: Possible values include: 'Absolute', 'Property'
    :type right_operand_type: str or ~lusid.models.enum
    """

    _attribute_map = {
        'left': {'key': 'left', 'type': 'str'},
        'operator': {'key': 'operator', 'type': 'str'},
        'right': {'key': 'right', 'type': 'object'},
        'right_operand_type': {'key': 'rightOperandType', 'type': 'str'},
    }

    def __init__(self, left=None, operator=None, right=None, right_operand_type=None):
        super(PropertyFilter, self).__init__()
        self.left = left
        self.operator = operator
        self.right = right
        self.right_operand_type = right_operand_type
