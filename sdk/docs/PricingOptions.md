# PricingOptions

Options for controlling the default aspects and behaviour of the pricing engine.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_selection** | [**ModelSelection**](ModelSelection.md) |  | [optional] 
**use_instrument_type_to_determine_pricer** | **bool** | If true then use the instrument type to set the default instrument pricer  This applies where no more specific set of overrides are provided on a per-vendor and instrument basis. | [optional] 
**allow_any_instruments_with_sec_uid_to_price_off_lookup** | **bool** | By default, one would not expect to price and exotic instrument, i.e. an instrument with a complicated  instrument definition simply through looking up a price as there should be a better way of evaluating it.  To override that behaviour and allow lookup for a price from the instrument identifier(s), set this to true. | [optional] 
**allow_partially_successful_evaluation** | **bool** | If true then a failure in task evaluation doesn&#39;t cause overall failure.  results will be returned where they succeeded and annotation elsewhere | [optional] 
**produce_separate_result_for_linear_otc_legs** | **bool** | If true (default), when pricing an Fx-Forward or Interest Rate Swap, Future and other linearly separable products, product two results, one for each leg  rather than a single line result with the amalgamated/summed pv from both legs. | [optional] 
**enable_use_of_cached_unit_results** | **bool** | If true, when pricing using a model or for an instrument that supports use of intermediate cached-results, use them.  Default is that this caching is turned off. | [optional] 
**window_valuation_on_instrument_start_end** | **bool** | If true, when valuing an instrument outside the period where it is &#39;alive&#39; (the start-maturity window) it will return a valuation of zero | [optional] 
**remove_contingent_cashflows_in_payment_diary** | **bool** | When creating a payment diary, should contingent cash payments (e.g. from exercise of a swaption into a swap) be included or not.  i.e. Is exercise or default being assumed to happen or not. | [optional] 
**use_child_sub_holding_keys_for_portfolio_expansion** | **bool** | Should fund constituents inherit subholding keys from the parent subholding keyb | [optional] 
**validate_domestic_and_quote_currencies_are_consistent** | **bool** | Do we validate that the instrument domestic currency matches the quote currency (unless unknown/zzz) when using lookup pricing. | [optional] 
**conserved_quantity_for_lookthrough_expansion** | **str** | When performing lookthrough portfolio expansion with ScalingMethodology set to \&quot;Sum\&quot; or \&quot;AbsoluteSum\&quot;,  the quantity specified here will be conserved and apportioned to lookthrough constituents.  For example, an equal-weighting index with 100 constituents can be modelled as a reference portfolio with 1% weights on each equity.  When expanding a $9000 holding of that index into its constituents while conserving PV, we end up with $90 of each equity.  The number of units of each equity held is then implied.  Note that conservation of one quantity may imply non-conservation of others, especially when some constituents are OTCs.                Allowed values are: \&quot;PV\&quot; (default), \&quot;Exposure\&quot;. | [optional] 

## Example

```python
from lusid.models.pricing_options import PricingOptions

# TODO update the JSON string below
json = "{}"
# create an instance of PricingOptions from a JSON string
pricing_options_instance = PricingOptions.from_json(json)
# print the JSON string representation of the object
print PricingOptions.to_json()

# convert the object into a dict
pricing_options_dict = pricing_options_instance.to_dict()
# create an instance of PricingOptions from a dict
pricing_options_form_dict = pricing_options.from_dict(pricing_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


