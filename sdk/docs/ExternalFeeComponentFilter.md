# ExternalFeeComponentFilter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_id** | **str** |  | 
**filter** | **str** |  | 
**applies_to** | **str** |  | 
## Example

```python
from lusid.models.external_fee_component_filter import ExternalFeeComponentFilter
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr, validator

filter_id: StrictStr = "example_filter_id"
filter: StrictStr = "example_filter"
applies_to: StrictStr = "example_applies_to"
external_fee_component_filter_instance = ExternalFeeComponentFilter(filter_id=filter_id, filter=filter, applies_to=applies_to)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

