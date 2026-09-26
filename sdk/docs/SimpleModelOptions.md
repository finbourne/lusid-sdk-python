# SimpleModelOptions

Model options for a minimal pricer, allowing accrued interest calculation to be disabled and  the price quote to be interpreted as an offset from par.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assume_accrued_is_zero** | **bool** | Disable calculation for accrued interest  The simple static pricer will attempt to calculate accrued interest where an instrument is present  and the accrued is requested. This may no be what is desired. If the user is sure they just want lookup  pricing then they can disable the accrued interest calculation attempt.  If set, the override accrued will be used if given but the calculation for accrued will just return zero.  This will also disable requesting any required instrument dependencies (e.g. resets) that might be required  to calculate accrued. | [optional] 
**price_is_par_offset** | **bool** | Interpret the instrument&#39;s price quote as an offset from par rather than as a currency value for  one unit of notional. The unit value becomes (price - basis) / basis, so a quote at par gives a  unit value of zero. The basis is taken from the quote&#39;s own scale factor, or 100 when the quote carries none.  This is not the treatment a bond price receives: a bond price is a proportion of par and scales  its value, whereas here only the distance from par carries value.  Supported for an interest rate swap only; setting it for any other instrument type fails the  valuation.  Quotes provided must have a quote type of either Price or DirtyPrice. The resulting unit  value is then the clean PV for a Price quote and the dirty PV for a DirtyPrice quote,  with accrued giving the other.  The quote must describe the swap as it is defined. The legs&#39; pay and receive directions do not  sign the value taken from the quote, so a swap booked the other way round is expected to be  quoted the other side of par. | [optional] 
**model_options_type** | **str** | Available values: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, CdsModelOptions, FlexibleLoanPricerOptions, HullWhiteModelOptions, BondLookupModelOptions, BondForwardModelOptions, SimpleModelOptions. | 
## Example

```python
from lusid.models.simple_model_options import SimpleModelOptions
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

assume_accrued_is_zero: Optional[StrictBool] = # Replace with your value
assume_accrued_is_zero:Optional[StrictBool] = None
price_is_par_offset: Optional[StrictBool] = # Replace with your value
price_is_par_offset:Optional[StrictBool] = None
model_options_type: StrictStr = "example_model_options_type"
simple_model_options_instance = SimpleModelOptions(assume_accrued_is_zero=assume_accrued_is_zero, price_is_par_offset=price_is_par_offset, model_options_type=model_options_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

