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


class PricingContext(Model):
    """Pricing context node. In order to price an instrument a number of
    configuration parameters are required to determine which
    (a) pricing model (ranging from a simple lookup of a market quote/price
    through to a Monte-Carlo simulation for the behaviour of its cashflows)
    (b) vendor library (Lusid internal models or those provided through an
    external Vendor such as Refinitiv (proprietary) or QuantLib (open source)
    are used in the pricing.
    In conjunction with these there are a number of parameters that govern the
    behaviour of these models. For example, in pricing an Fx volatility
    dependent product such as an Fx option, there are various parameters that
    affect model behaviour for the smile. In Lusid a distinction is made
    between
    those which are understood natively and those which are only held for use
    with a given vendor-model combination. The problem is that, unlike market
    quote data, there are few standards around model descriptions. Hence,
    apparently similar terminology can be mis-leading; for example in SABR
    models where
    the basic parameters are agreed upon but most practical models have used an
    approximation with adjustments where the parameters can have wildly
    different meanings.
    To avoid confusion or mis-behaviour in this area, where parameters are not
    understood to be interchangeable, they are only settable on a per-library
    per-model
    basis, essentially as opaque data that will be given to the Vendor library
    "verbatim" but not used with any other.

    :param model_rules: The set of model rules that are available. There may
     be multiple rules for Vendors, but only one per model-instrument pair.
     Which of these preference sets is used depends upon the model choice
     selection if specified, or failing that the global default model
     specification
     in the options.
    :type model_rules: list[~lusid.models.VendorModelRule]
    :param model_choice: The choice of which model selection (vendor library,
     pricing model) to use in evaluation of a given instrument type.
    :type model_choice: dict[str, ~lusid.models.ModelSelection]
    :param options: Miscellaneous options for controlling pricing.
    :type options: ~lusid.models.PricingOptions
    """

    _attribute_map = {
        'model_rules': {'key': 'modelRules', 'type': '[VendorModelRule]'},
        'model_choice': {'key': 'modelChoice', 'type': '{ModelSelection}'},
        'options': {'key': 'options', 'type': 'PricingOptions'},
    }

    def __init__(self, model_rules=None, model_choice=None, options=None):
        super(PricingContext, self).__init__()
        self.model_rules = model_rules
        self.model_choice = model_choice
        self.options = options
