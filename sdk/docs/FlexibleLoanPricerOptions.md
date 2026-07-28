# FlexibleLoanPricerOptions

Model options for instruments of type flexibleDeposit and flexibleLoan when used on a standalone basis.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set_clean_pvto_zero** | **bool** | If set to true the CleanPV will be set to zero in valuations and PV will effectively just be the Accrual. | 
**model_options_type** | **str** | Available values: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, CdsModelOptions, FlexibleLoanPricerOptions. | 
## Example

```python
from lusid.models.flexible_loan_pricer_options import FlexibleLoanPricerOptions
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

set_clean_pvto_zero: StrictBool = # Replace with your value
set_clean_pvto_zero:StrictBool = True
model_options_type: StrictStr = "example_model_options_type"
flexible_loan_pricer_options_instance = FlexibleLoanPricerOptions(set_clean_pvto_zero=set_clean_pvto_zero, model_options_type=model_options_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

