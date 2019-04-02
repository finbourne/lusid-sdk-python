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


class ModelSelection(Model):
    """The combination of a library to use and a model in that library that
    defines which pricing code will evaluate instruments
    having a particular type/class. This allows us to control the model type
    and library for a given instrument.

    :param library: Which library is used for pricing requests. Possible
     values include: 'Lusid', 'ReutersEikon', 'ReutersTracsWeb'
    :type library: str or ~lusid.models.enum
    :param model: Which model should be used for pricing requests. Possible
     values include: 'SimpleStatic', 'Discounting', 'VendorDefault'
    :type model: str or ~lusid.models.enum
    """

    _validation = {
        'library': {'required': True},
        'model': {'required': True},
    }

    _attribute_map = {
        'library': {'key': 'library', 'type': 'str'},
        'model': {'key': 'model', 'type': 'str'},
    }

    def __init__(self, library, model):
        super(ModelSelection, self).__init__()
        self.library = library
        self.model = model
