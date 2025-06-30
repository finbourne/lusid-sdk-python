# EligibilityCalculation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entitlement_date** | **str** |  | 
**eligible_units** | **str** |  | 
**date_modifiable_by_instruction** | **bool** |  | [optional] 
## Example

```python
from lusid.models.eligibility_calculation import EligibilityCalculation
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, constr

entitlement_date: StrictStr = "example_entitlement_date"
eligible_units: StrictStr = "example_eligible_units"
date_modifiable_by_instruction: Optional[StrictBool] = # Replace with your value
date_modifiable_by_instruction:Optional[StrictBool] = None
eligibility_calculation_instance = EligibilityCalculation(entitlement_date=entitlement_date, eligible_units=eligible_units, date_modifiable_by_instruction=date_modifiable_by_instruction)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

