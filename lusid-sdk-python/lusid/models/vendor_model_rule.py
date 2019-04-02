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


class VendorModelRule(Model):
    """A rule that identifies the set of preferences to be used for a given
    library, model and instrument type.
    There can be many such rules, though only the first found for a given
    combination would be used.

    :param supplier: The vendor library supplier. Possible values include:
     'Lusid', 'ReutersEikon', 'ReutersTracsWeb'
    :type supplier: str or ~lusid.models.enum
    :param model_name: The vendor library model name
    :type model_name: str
    :param instrument_type: The vendor library instrument type
    :type instrument_type: str
    :param parameters: The set of opaque model parameters, provided as a Json
     object, that is a string object which will internally be converted to a
     dictionary of string to object.
     Note that this is not intended as the final form of this object. It will
     be replaced with a more structured object as the set of parameters that
     are possible is
     better understood.
    :type parameters: str
    """

    _validation = {
        'supplier': {'required': True},
        'model_name': {'required': True},
        'instrument_type': {'required': True},
        'parameters': {'required': True},
    }

    _attribute_map = {
        'supplier': {'key': 'supplier', 'type': 'str'},
        'model_name': {'key': 'modelName', 'type': 'str'},
        'instrument_type': {'key': 'instrumentType', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': 'str'},
    }

    def __init__(self, supplier, model_name, instrument_type, parameters):
        super(VendorModelRule, self).__init__()
        self.supplier = supplier
        self.model_name = model_name
        self.instrument_type = instrument_type
        self.parameters = parameters
