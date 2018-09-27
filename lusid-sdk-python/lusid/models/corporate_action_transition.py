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


class CorporateActionTransition(Model):
    """A 'transition' within a corporate action, representing a set of output
    movements paired to a single input position.

    :param input_transition:
    :type input_transition: ~lusid.models.CorporateActionTransitionComponent
    :param output_transitions:
    :type output_transitions:
     list[~lusid.models.CorporateActionTransitionComponent]
    """

    _attribute_map = {
        'input_transition': {'key': 'inputTransition', 'type': 'CorporateActionTransitionComponent'},
        'output_transitions': {'key': 'outputTransitions', 'type': '[CorporateActionTransitionComponent]'},
    }

    def __init__(self, input_transition=None, output_transitions=None):
        super(CorporateActionTransition, self).__init__()
        self.input_transition = input_transition
        self.output_transitions = output_transitions
