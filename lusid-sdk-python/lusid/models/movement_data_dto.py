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


class MovementDataDto(Model):
    """MovementDataDto.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar movement_types: The movement types. Possible values include:
     'Settlement', 'Traded', 'ForwardFx', 'Commitment', 'Receivable',
     'CashSettlement', 'Accrual'
    :vartype movement_types: str or ~lusid.models.enum
    :ivar side: The Side. Possible values include: 'Side1', 'Side2', 'BondInt'
    :vartype side: str or ~lusid.models.enum
    :ivar direction:
    :vartype direction: int
    :ivar flags: The Flags
    :vartype flags: str
    """

    _validation = {
        'movement_types': {'required': True, 'readonly': True},
        'side': {'required': True, 'readonly': True},
        'direction': {'required': True, 'readonly': True},
        'flags': {'required': True, 'readonly': True},
    }

    _attribute_map = {
        'movement_types': {'key': 'movementTypes', 'type': 'str'},
        'side': {'key': 'side', 'type': 'str'},
        'direction': {'key': 'direction', 'type': 'int'},
        'flags': {'key': 'flags', 'type': 'str'},
    }

    def __init__(self):
        super(MovementDataDto, self).__init__()
        self.movement_types = None
        self.side = None
        self.direction = None
        self.flags = None
