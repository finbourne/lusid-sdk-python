# AccessMetadataValue

An access control value. Provider should only be used if you are a service provider licensing data. In that case  the provider value must match your domain.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | 
**provider** | **str** |  | [optional] 
## Example

```python
from lusid.models.access_metadata_value import AccessMetadataValue
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr

value: StrictStr = "example_value"
provider: Optional[StrictStr] = "example_provider"
access_metadata_value_instance = AccessMetadataValue(value=value, provider=provider)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

