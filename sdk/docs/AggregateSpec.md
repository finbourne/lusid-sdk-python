# AggregateSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key that uniquely identifies a queryable address in Lusid. | 
**op** | **str** | The available values are: Sum, DefaultSum, Proportion, Average, Count, Min, Max, Value, SumOfPositiveValues, SumOfNegativeValues, SumOfAbsoluteValues, ProportionOfAbsoluteValues, SumCumulativeInAdvance, SumCumulativeInArrears | 
**options** | **Dict[str, object]** | Additional options to apply when performing computations. Options that do not apply to the Key will be ignored. Option values can be boolean, numeric, string or date-time. | [optional] 
## Example

```python
from lusid.models.aggregate_spec import AggregateSpec
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, validator

key: StrictStr = "example_key"
op: StrictStr = "example_op"
options: Optional[Dict[str, Any]] = # Replace with your value
aggregate_spec_instance = AggregateSpec(key=key, op=op, options=options)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

