# ShareClassData

The data for a Share Class. Includes Valuation Point Data and instrument information.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**share_class_breakdown** | [**ShareClassBreakdown**](ShareClassBreakdown.md) |  | 
**share_class_details** | [**ShareClassDetails**](ShareClassDetails.md) |  | [optional] 
## Example

```python
from lusid.models.share_class_data import ShareClassData
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

share_class_breakdown: ShareClassBreakdown = # Replace with your value
share_class_details: Optional[ShareClassDetails] = # Replace with your value
share_class_data_instance = ShareClassData(share_class_breakdown=share_class_breakdown, share_class_details=share_class_details)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

