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


class InstrumentMatch(Model):
    """InstrumentMatch.

    :param name: The name of the instrument
    :type name: str
    :param identifiers: The set of identifiers that uniquely identify this
     instrument
    :type identifiers: dict[str, str]
    :param properties: Any requested properties are decorated on the
     instrument, and will have a value of
     'Unknown', if no value was found for this instrument.
    :type properties: list[~lusid.models.Property]
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'identifiers': {'key': 'identifiers', 'type': '{str}'},
        'properties': {'key': 'properties', 'type': '[Property]'},
    }

    def __init__(self, name=None, identifiers=None, properties=None):
        super(InstrumentMatch, self).__init__()
        self.name = name
        self.identifiers = identifiers
        self.properties = properties
