# RecResultItemDetails

The individual items that make up a rec result, split by side. Zero counts and empty arrays for  results that have cleared.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count_left** | **int** | The number of items grouped on the left side. | 
**count_right** | **int** | The number of items grouped on the right side. | 
**left** | [**List[RecResultItem]**](RecResultItem.md) | The left-side items. | [optional] 
**right** | [**List[RecResultItem]**](RecResultItem.md) | The right-side items. | [optional] 
## Example

```python
from lusid.models.rec_result_item_details import RecResultItemDetails
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

count_left: StrictInt = # Replace with your value
count_left: StrictInt = 42
count_right: StrictInt = # Replace with your value
count_right: StrictInt = 42
left: Optional[List[RecResultItem]] = # Replace with your value
right: Optional[List[RecResultItem]] = # Replace with your value
rec_result_item_details_instance = RecResultItemDetails(count_left=count_left, count_right=count_right, left=left, right=right)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

