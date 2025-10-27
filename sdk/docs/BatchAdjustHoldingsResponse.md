# BatchAdjustHoldingsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**Dict[str, HoldingAdjustmentWithDate]**](HoldingAdjustmentWithDate.md) | The holdings which have been successfully adjusted. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The holdings that could not be adjusted along with a reason for their failure. | [optional] 
**metadata** | **Dict[str, Optional[List[ResponseMetaData]]]** | Contains warnings related to adjusted holdings | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.batch_adjust_holdings_response import BatchAdjustHoldingsResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

values: Optional[Dict[str, HoldingAdjustmentWithDate]] = # Replace with your value
failed: Optional[Dict[str, ErrorDetail]] = # Replace with your value
metadata: Optional[Dict[str, Optional[List[ResponseMetaData]]]] = # Replace with your value
links: Optional[List[Link]] = None
batch_adjust_holdings_response_instance = BatchAdjustHoldingsResponse(values=values, failed=failed, metadata=metadata, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

