# UpdateMarketDataFieldConfigurationRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add** | [**MetadataFieldsToAdd**](MetadataFieldsToAdd.md) |  | [optional] 
**update** | [**MetadataFieldsToUpdate**](MetadataFieldsToUpdate.md) |  | [optional] 
**remove** | [**MetadataFieldsToRemove**](MetadataFieldsToRemove.md) |  | [optional] 
## Example

```python
from lusid.models.update_market_data_field_configuration_request import UpdateMarketDataFieldConfigurationRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

add: Optional[MetadataFieldsToAdd] = None
update: Optional[MetadataFieldsToUpdate] = None
remove: Optional[MetadataFieldsToRemove] = None
update_market_data_field_configuration_request_instance = UpdateMarketDataFieldConfigurationRequest(add=add, update=update, remove=remove)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

