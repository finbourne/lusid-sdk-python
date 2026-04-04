# AllocationGroupClassDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**share_class_short_code** | **str** | A short code that uniquely identifies the share class within the Fund and is attached to the transaction. | 
**share_class_fund_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**apportionment_factor** | **float** | The weighting factor used for apportionment across this share class. | [optional] 
**share_class_series_code** | **str** | An optional series identifier for the share class. If not provided, the share class will include all series. | [optional] 
## Example

```python
from lusid.models.allocation_group_class_definition import AllocationGroupClassDefinition
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

share_class_short_code: StrictStr = "example_share_class_short_code"
share_class_fund_id: Optional[ResourceId] = # Replace with your value
apportionment_factor: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
share_class_series_code: Optional[StrictStr] = "example_share_class_series_code"
allocation_group_class_definition_instance = AllocationGroupClassDefinition(share_class_short_code=share_class_short_code, share_class_fund_id=share_class_fund_id, apportionment_factor=apportionment_factor, share_class_series_code=share_class_series_code)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

