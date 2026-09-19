# FractionalUnitsTrueUpConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fractional_units_handling** | **str** | The fractional-units handling scheme for the portfolio&#39;s corporate-action processing. This can be: LotLevelRounding or CustodianLevelTrueUp. Defaults to LotLevelRounding, today&#39;s per-lot-only processing, if not specified. Available values: LotLevelRounding, CustodianLevelTrueUp. | [optional] 
**nominated_sub_holding_key** | **str** | The sub-holding key (from the &#39;Transaction&#39; domain) that custodian-level fractional-units true-ups are booked to. The key must be one of the portfolio&#39;s sub-holding keys, must have a pre-defined property definition, and event processing never creates it. | [optional] 
**nominated_sub_holding_key_value** | **str** | The value of the nominated sub-holding key under which the true-up holding is booked, for example the bucket that quarantines fractional rounding true-ups. | [optional] 
## Example

```python
from lusid.models.fractional_units_true_up_configuration import FractionalUnitsTrueUpConfiguration
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

fractional_units_handling: Optional[StrictStr] = "example_fractional_units_handling"
nominated_sub_holding_key: Optional[StrictStr] = "example_nominated_sub_holding_key"
nominated_sub_holding_key_value: Optional[StrictStr] = "example_nominated_sub_holding_key_value"
fractional_units_true_up_configuration_instance = FractionalUnitsTrueUpConfiguration(fractional_units_handling=fractional_units_handling, nominated_sub_holding_key=nominated_sub_holding_key, nominated_sub_holding_key_value=nominated_sub_holding_key_value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

