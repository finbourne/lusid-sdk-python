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


class PricingOptions(Model):
    """Options for controlling the default aspects and behaviour of the pricing
    engine.

    :param model_selection: The default model and pricing library to use if no
     others specified
    :type model_selection: ~lusid.models.ModelSelection
    :param allow_partially_successful_evaluation: If true then a failure in
     task evaluation doesn't cause overall failure.
     results will be returned where they succeeded and annotation elsewhere
    :type allow_partially_successful_evaluation: bool
    """

    _attribute_map = {
        'model_selection': {'key': 'modelSelection', 'type': 'ModelSelection'},
        'allow_partially_successful_evaluation': {'key': 'allowPartiallySuccessfulEvaluation', 'type': 'bool'},
    }

    def __init__(self, model_selection=None, allow_partially_successful_evaluation=None):
        super(PricingOptions, self).__init__()
        self.model_selection = model_selection
        self.allow_partially_successful_evaluation = allow_partially_successful_evaluation
