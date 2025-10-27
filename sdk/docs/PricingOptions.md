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
**mbs_valuation_using_holding_current_face** | **bool** |  | [optional] 
**convert_srs_cash_flows_to_portfolio_currency** | **bool** | In the case upserted structured result store (SRS) cashflows are not   in the portfolio currency, set this parameter to True to convert said  cashflows into the portfolio currency. By default, this flag is set   to False and Lusid will not do any FX conversion.    Please note that FX conversion is dependent on the data available in  the quote store - ensure that all relevant FX quotes have been loaded  for cashflow currency conversion. | [optional] 
**conserved_quantity_for_lookthrough_expansion** | **str** | When performing lookthrough portfolio expansion with ScalingMethodology set to \&quot;Sum\&quot; or \&quot;AbsoluteSum\&quot;,  the quantity specified here will be conserved and apportioned to lookthrough constituents.  For example, an equal-weighting index with 100 constituents can be modelled as a reference portfolio with 1% weights on each equity.  When expanding a $9000 holding of that index into its constituents while conserving PV, we end up with $90 of each equity.  The number of units of each equity held is then implied.  Note that conservation of one quantity may imply non-conservation of others, especially when some constituents are OTCs.                Allowed values are: \&quot;PV\&quot; (default), \&quot;Exposure\&quot;. | [optional] 
**return_zero_pv** | [**ReturnZeroPvOptions**](ReturnZeroPvOptions.md) |  | [optional] 
**enable_leg_level_inference_for_custom_srs_columns** | **bool** | When enabled, allows inference between leg-level and  instrument-level data during portfolio valuation. If  data is missing at one level, it may be inferred from  the other level. For example, missing leg-level data   may be inferred from existing leg-level and instrument-  level data when ProduceSeparateResultForLinearOtcLegs  is enabled, and vice versa. Explicitly provided data  always takes precedence. | [optional] 
**use_instrument_scale_factor_as_default** | **bool** | When enabled, priceScaleFactor defined at the instrument level will  be used in the absence of quote scaleFactor when resolving quotes. | [optional] 
## Example

```python
from lusid.models.pricing_options import PricingOptions
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

model_selection: Optional[ModelSelection] = # Replace with your value
use_instrument_type_to_determine_pricer: Optional[StrictBool] = # Replace with your value
use_instrument_type_to_determine_pricer:Optional[StrictBool] = None
allow_any_instruments_with_sec_uid_to_price_off_lookup: Optional[StrictBool] = # Replace with your value
allow_any_instruments_with_sec_uid_to_price_off_lookup:Optional[StrictBool] = None
allow_partially_successful_evaluation: Optional[StrictBool] = # Replace with your value
allow_partially_successful_evaluation:Optional[StrictBool] = None
produce_separate_result_for_linear_otc_legs: Optional[StrictBool] = # Replace with your value
produce_separate_result_for_linear_otc_legs:Optional[StrictBool] = None
enable_use_of_cached_unit_results: Optional[StrictBool] = # Replace with your value
enable_use_of_cached_unit_results:Optional[StrictBool] = None
window_valuation_on_instrument_start_end: Optional[StrictBool] = # Replace with your value
window_valuation_on_instrument_start_end:Optional[StrictBool] = None
remove_contingent_cashflows_in_payment_diary: Optional[StrictBool] = # Replace with your value
remove_contingent_cashflows_in_payment_diary:Optional[StrictBool] = None
use_child_sub_holding_keys_for_portfolio_expansion: Optional[StrictBool] = # Replace with your value
use_child_sub_holding_keys_for_portfolio_expansion:Optional[StrictBool] = None
validate_domestic_and_quote_currencies_are_consistent: Optional[StrictBool] = # Replace with your value
validate_domestic_and_quote_currencies_are_consistent:Optional[StrictBool] = None
mbs_valuation_using_holding_current_face: Optional[StrictBool] = # Replace with your value
mbs_valuation_using_holding_current_face:Optional[StrictBool] = None
convert_srs_cash_flows_to_portfolio_currency: Optional[StrictBool] = # Replace with your value
convert_srs_cash_flows_to_portfolio_currency:Optional[StrictBool] = None
conserved_quantity_for_lookthrough_expansion: Optional[StrictStr] = "example_conserved_quantity_for_lookthrough_expansion"
return_zero_pv: Optional[ReturnZeroPvOptions] = # Replace with your value
enable_leg_level_inference_for_custom_srs_columns: Optional[StrictBool] = # Replace with your value
enable_leg_level_inference_for_custom_srs_columns:Optional[StrictBool] = None
use_instrument_scale_factor_as_default: Optional[StrictBool] = # Replace with your value
use_instrument_scale_factor_as_default:Optional[StrictBool] = None
pricing_options_instance = PricingOptions(model_selection=model_selection, use_instrument_type_to_determine_pricer=use_instrument_type_to_determine_pricer, allow_any_instruments_with_sec_uid_to_price_off_lookup=allow_any_instruments_with_sec_uid_to_price_off_lookup, allow_partially_successful_evaluation=allow_partially_successful_evaluation, produce_separate_result_for_linear_otc_legs=produce_separate_result_for_linear_otc_legs, enable_use_of_cached_unit_results=enable_use_of_cached_unit_results, window_valuation_on_instrument_start_end=window_valuation_on_instrument_start_end, remove_contingent_cashflows_in_payment_diary=remove_contingent_cashflows_in_payment_diary, use_child_sub_holding_keys_for_portfolio_expansion=use_child_sub_holding_keys_for_portfolio_expansion, validate_domestic_and_quote_currencies_are_consistent=validate_domestic_and_quote_currencies_are_consistent, mbs_valuation_using_holding_current_face=mbs_valuation_using_holding_current_face, convert_srs_cash_flows_to_portfolio_currency=convert_srs_cash_flows_to_portfolio_currency, conserved_quantity_for_lookthrough_expansion=conserved_quantity_for_lookthrough_expansion, return_zero_pv=return_zero_pv, enable_leg_level_inference_for_custom_srs_columns=enable_leg_level_inference_for_custom_srs_columns, use_instrument_scale_factor_as_default=use_instrument_scale_factor_as_default)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

