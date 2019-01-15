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


class InstrumentDefinition(Model):
    """InstrumentDefinition.

    :param name: Required. The name of the instrument
    :type name: str
    :param identifiers: Required. A set of identifiers that uniquely identify
     this instrument (e.g FIGI, RIC)
    :type identifiers: dict[str, str]
    :param properties: Optional. A collection of properties to upsert on the
     instrument.
    :type properties: list[~lusid.models.InstrumentProperty]
    :param look_through_portfolio_id: Optional. The identifier of the
     portfolio that represents this instrument
    :type look_through_portfolio_id: ~lusid.models.ResourceId
    :param definition: Expanded instrument definition - in the case of OTC
     instruments
     this contains the definition of the non-exchange traded instrument.
     The format for this can be client-defined, but in order to transparently
     use
     vendor libraries it must conform to a format that LUSID understands.
    :type definition: ~lusid.models.InstrumentEconomicDefinition
    """

    _validation = {
        'name': {'required': True},
        'identifiers': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'identifiers': {'key': 'identifiers', 'type': '{str}'},
        'properties': {'key': 'properties', 'type': '[InstrumentProperty]'},
        'look_through_portfolio_id': {'key': 'lookThroughPortfolioId', 'type': 'ResourceId'},
        'definition': {'key': 'definition', 'type': 'InstrumentEconomicDefinition'},
    }

    def __init__(self, name, identifiers, properties=None, look_through_portfolio_id=None, definition=None):
        super(InstrumentDefinition, self).__init__()
        self.name = name
        self.identifiers = identifiers
        self.properties = properties
        self.look_through_portfolio_id = look_through_portfolio_id
        self.definition = definition
