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


class InstrumentProperty(Model):
    """InstrumentProperty.

    :param lusid_instrument_id: Unique instrument identifier
    :type lusid_instrument_id: str
    :param properties: A collection of properties to create or update
    :type properties: list[~lusid.models.CreateInstrumentPropertyRequest]
    :param deleted_properties: A collection of property keys to remove
     property values from, if any are set for the instrument
    :type deleted_properties:
     list[~lusid.models.DeleteInstrumentPropertyRequest]
    """

    _attribute_map = {
        'lusid_instrument_id': {'key': 'lusidInstrumentId', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '[CreateInstrumentPropertyRequest]'},
        'deleted_properties': {'key': 'deletedProperties', 'type': '[DeleteInstrumentPropertyRequest]'},
    }

    def __init__(self, lusid_instrument_id=None, properties=None, deleted_properties=None):
        super(InstrumentProperty, self).__init__()
        self.lusid_instrument_id = lusid_instrument_id
        self.properties = properties
        self.deleted_properties = deleted_properties
