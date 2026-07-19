# ApportionmentBreakdown

The apportionment result for one level - the fund (apportioning the non-class-specific P&L across all  share classes) or a single allocation group (apportioning its tagged P&L across its members) - with the  per-member base values and factors the method produced.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apportionment_level** | **str** | Whether this result is the fund-level apportionment (across all share classes) or an allocation group&#39;s (across its share classes). Available values: Fund, AllocationGroup. | 
**allocation_group_code** | **str** | The ShareClassShortCode identifying the allocation group this result is for, or null for the fund-level result. | [optional] 
**apportionment_method_property_key** | **str** | The apportionment method property key that produced the factors. | 
**factors** | [**List[ApportionmentMemberFactor]**](ApportionmentMemberFactor.md) | The per-member base values and apportionment factors produced by the method. | 
## Example

```python
from lusid.models.apportionment_breakdown import ApportionmentBreakdown
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

apportionment_level: StrictStr = "example_apportionment_level"
allocation_group_code: Optional[StrictStr] = "example_allocation_group_code"
apportionment_method_property_key: StrictStr = "example_apportionment_method_property_key"
factors: List[ApportionmentMemberFactor] = # Replace with your value
apportionment_breakdown_instance = ApportionmentBreakdown(apportionment_level=apportionment_level, allocation_group_code=allocation_group_code, apportionment_method_property_key=apportionment_method_property_key, factors=factors)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

