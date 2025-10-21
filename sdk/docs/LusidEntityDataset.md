# LusidEntityDataset

Contains the run-time parameters that are appropriate for check definitions  with datasetSchema.type = \"LusidEntity\"
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_at** | **datetime** | The asAt date to fetch the data. Nullable. Defaults to latest. | [optional] 
**effective_at** | **datetime** | The effectiveAt date to fetch the data. Nullable. Defaults to latest. | [optional] 
**scope** | **str** | The scope of the entities to check. Required. | 
**as_at_modified_since** | **datetime** | Nullable. Filters the dataset for version.asAtModified greater than or equal to this value. | [optional] 
**selector_attribute** | **str** | An attribute (field name, propertyKey or identifierKey) to use to sub-divide the dataset. | 
**selector_value** | **str** | The value of the above attribute used to sub-divide the dataset. | 
**return_identifier_key** | **str** | The preferred identifier to return for entities with multiple external identifiers. | [optional] 
## Example

```python
from lusid.models.lusid_entity_dataset import LusidEntityDataset
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr, validator
from datetime import datetime
as_at: Optional[datetime] = # Replace with your value
effective_at: Optional[datetime] = # Replace with your value
scope: StrictStr = "example_scope"
as_at_modified_since: Optional[datetime] = # Replace with your value
selector_attribute: StrictStr = "example_selector_attribute"
selector_value: StrictStr = "example_selector_value"
return_identifier_key: Optional[StrictStr] = "example_return_identifier_key"
lusid_entity_dataset_instance = LusidEntityDataset(as_at=as_at, effective_at=effective_at, scope=scope, as_at_modified_since=as_at_modified_since, selector_attribute=selector_attribute, selector_value=selector_value, return_identifier_key=return_identifier_key)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

