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


class CreateClientInstrumentRequest(Model):
    """CreateClientInstrumentRequest.

    :param client_instrument_id:
    :type client_instrument_id: str
    :param name:
    :type name: str
    :param instrument_properties:
    :type instrument_properties: dict[str,
     ~lusid.models.CreatePropertyRequest]
    :param look_through_portfolio_id:
    :type look_through_portfolio_id: ~lusid.models.ResourceId
    :param instrument: There could be multiple underlying instrument
     definitions (same
     instrument but different format), but for now store one.
    :type instrument: ~lusid.models.InstrumentDefinitionDto
    """

    _validation = {
        'client_instrument_id': {'required': True},
        'name': {'required': True},
        'instrument_properties': {'required': True},
    }

    _attribute_map = {
        'client_instrument_id': {'key': 'clientInstrumentId', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'instrument_properties': {'key': 'instrumentProperties', 'type': '{CreatePropertyRequest}'},
        'look_through_portfolio_id': {'key': 'lookThroughPortfolioId', 'type': 'ResourceId'},
        'instrument': {'key': 'instrument', 'type': 'InstrumentDefinitionDto'},
    }

    def __init__(self, client_instrument_id, name, instrument_properties, look_through_portfolio_id=None, instrument=None):
        super(CreateClientInstrumentRequest, self).__init__()
        self.client_instrument_id = client_instrument_id
        self.name = name
        self.instrument_properties = instrument_properties
        self.look_through_portfolio_id = look_through_portfolio_id
        self.instrument = instrument
