# ValuationPointDataRequest

The ValuationPointDataRequest.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diary_entry_code** | **str** | Unique code for the Valuation Point. | 
## Example

```python
from lusid.models.valuation_point_data_request import ValuationPointDataRequest
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr, validator

diary_entry_code: StrictStr = "example_diary_entry_code"
valuation_point_data_request_instance = ValuationPointDataRequest(diary_entry_code=diary_entry_code)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

