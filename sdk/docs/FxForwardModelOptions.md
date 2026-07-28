# FxForwardModelOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forward_rate_observable_type** | **str** | Available values: ForwardPoints, ForwardRate, RatesCurve, FxForwardCurve, Invalid. | 
**discounting_method** | **str** | Available values: Standard, ConstantTimeValueOfMoney, Invalid. | 
**convert_to_report_ccy** | **bool** | Convert all FX flows to the report currency  By setting this all FX forwards will be priced using Forward Curves that have Report Currency as the base. | 
**allow_spot_fallback_for_report_ccy** | **bool** | When converting to the report currency, allow falling back to pricing off the natural-pair forward  and converting to the report currency at spot when the report-currency cross forward curves are not  available. Defaults to false, in which case the report-currency cross forwards are required. | [optional] 
**model_options_type** | **str** | Available values: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, CdsModelOptions, FlexibleLoanPricerOptions. | 
## Example

```python
from lusid.models.fx_forward_model_options import FxForwardModelOptions
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

forward_rate_observable_type: StrictStr = "example_forward_rate_observable_type"
discounting_method: StrictStr = "example_discounting_method"
convert_to_report_ccy: StrictBool = # Replace with your value
convert_to_report_ccy:StrictBool = True
allow_spot_fallback_for_report_ccy: Optional[StrictBool] = # Replace with your value
allow_spot_fallback_for_report_ccy:Optional[StrictBool] = None
model_options_type: StrictStr = "example_model_options_type"
fx_forward_model_options_instance = FxForwardModelOptions(forward_rate_observable_type=forward_rate_observable_type, discounting_method=discounting_method, convert_to_report_ccy=convert_to_report_ccy, allow_spot_fallback_for_report_ccy=allow_spot_fallback_for_report_ccy, model_options_type=model_options_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

