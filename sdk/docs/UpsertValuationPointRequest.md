# UpsertValuationPointRequest

A definition for the period you wish to close
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diary_entry_code** | **str** | Unique code for the Valuation Point. | 
**name** | **str** | Identifiable Name assigned to the Valuation Point. | [optional] 
**effective_at** | **datetime** | The effective time of the diary entry. | 
**query_as_at** | **datetime** | The query time of the diary entry. Defaults to latest. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties for the diary entry. | [optional] 
**apply_clear_down** | **bool** | Defaults to false. Set to true if you want that the closed period to have the clear down applied. | [optional] 
## Example

```python
from lusid.models.upsert_valuation_point_request import UpsertValuationPointRequest
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, constr, validator
from datetime import datetime
diary_entry_code: StrictStr = "example_diary_entry_code"
name: Optional[StrictStr] = "example_name"
effective_at: datetime = # Replace with your value
query_as_at: Optional[datetime] = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
apply_clear_down: Optional[StrictBool] = # Replace with your value
apply_clear_down:Optional[StrictBool] = None
upsert_valuation_point_request_instance = UpsertValuationPointRequest(diary_entry_code=diary_entry_code, name=name, effective_at=effective_at, query_as_at=query_as_at, properties=properties, apply_clear_down=apply_clear_down)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

