# FlexibleLoanPricerOptions

Model options for instruments of type flexibleDeposit and flexibleLoan when used on a standalone basis.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set_clean_pvto_zero** | **bool** | If set to true the CleanPV will be set to zero in valuations and PV will effectively just be the Accrual. | 
**use_price_quote_for_clean_pv** | **bool** | If set to true the CleanPV calculation will be looking for a price quote (no default price is assumed). CleanPV will be calculated as Holding/Balance * priceQuote / quoteScaleFactor | [optional] 
**exclude_income_from_pv** | **bool** | Read by a TotalReturnSwap whose asset leg has a ResetSchedule and whose underlying pays interest or coupons. If set to true the swap&#39;s PV leaves out the underlying&#39;s interest and coupon payments and adds the interest accrued on them to the valuation date instead, so CleanPV is the price return and PV is CleanPV + Accrued. | [optional] 
**funding_leg_accrued_only** | **bool** | Read by a TotalReturnSwap. If set to true the funding leg&#39;s PV is the interest it has accrued to the valuation date, in place of the coupons it has still to earn, so the swap carries no funding interest not yet earned: PV is the asset leg&#39;s PV plus the funding accrued, and CleanPV is PV less Accrued. A coupon already earned but not yet paid and a notional exchange keep the value they have with the option off. Under a funding notional reset the accrued is the re-struck one; an end-of-day valuation on a reset day whose reset is not yet stored re-strikes on the spot in its place, so the figure moves once that reset is stored. Supported by the price-return pricer (asset leg with a ResetSchedule) and by BondLookupPricer and FlexibleLoanPricer; refused for a swap without a ResetSchedule under ConstantTimeValueOfMoney or Discounting. | [optional] 
**model_options_type** | **str** | Available values: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, CdsModelOptions, FlexibleLoanPricerOptions, HullWhiteModelOptions, BondLookupModelOptions, BondForwardModelOptions, SimpleModelOptions, StripBondModelOptions. | 
## Example

```python
from lusid.models.flexible_loan_pricer_options import FlexibleLoanPricerOptions
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

set_clean_pvto_zero: StrictBool = # Replace with your value
set_clean_pvto_zero:StrictBool = True
use_price_quote_for_clean_pv: Optional[StrictBool] = # Replace with your value
use_price_quote_for_clean_pv:Optional[StrictBool] = None
exclude_income_from_pv: Optional[StrictBool] = # Replace with your value
exclude_income_from_pv:Optional[StrictBool] = None
funding_leg_accrued_only: Optional[StrictBool] = # Replace with your value
funding_leg_accrued_only:Optional[StrictBool] = None
model_options_type: StrictStr = "example_model_options_type"
flexible_loan_pricer_options_instance = FlexibleLoanPricerOptions(set_clean_pvto_zero=set_clean_pvto_zero, use_price_quote_for_clean_pv=use_price_quote_for_clean_pv, exclude_income_from_pv=exclude_income_from_pv, funding_leg_accrued_only=funding_leg_accrued_only, model_options_type=model_options_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

