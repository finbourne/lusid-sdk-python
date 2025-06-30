# UpsertPersonRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifiers** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The identifiers the person will be upserted with.The provided keys should be idTypeScope, idTypeCode, code | 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties associated to the Person. There can be multiple properties associated with a property key. | [optional] 
**display_name** | **str** | The display name of the Person | 
**description** | **str** | The description of the Person | [optional] 
## Example

```python
from lusid.models.upsert_person_request import UpsertPersonRequest
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr

identifiers: Dict[str, ModelProperty] = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
upsert_person_request_instance = UpsertPersonRequest(identifiers=identifiers, properties=properties, display_name=display_name, description=description)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

