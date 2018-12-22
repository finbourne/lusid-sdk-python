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
    """A collection of instrument search results.

    :param mastered_instruments: A collection of instruments that have met
     some criteria that have been previously
     mastered within LUSID
    :type mastered_instruments: list[~lusid.models.InstrumentDefinition]
    :param external_instruments: A collection of instruments that have met
     some criteria, but that have not been
     mastered within LUSID.
    :type external_instruments: list[~lusid.models.InstrumentDefinition]
    """

    _attribute_map = {
        'mastered_instruments': {'key': 'masteredInstruments', 'type': '[InstrumentDefinition]'},
        'external_instruments': {'key': 'externalInstruments', 'type': '[InstrumentDefinition]'},
    }

    def __init__(self, mastered_instruments=None, external_instruments=None):
        super(InstrumentMatch, self).__init__()
        self.mastered_instruments = mastered_instruments
        self.external_instruments = external_instruments
