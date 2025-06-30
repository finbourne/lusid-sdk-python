# BatchAdjustHoldingsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**Dict[str, HoldingAdjustmentWithDate]**](HoldingAdjustmentWithDate.md) | The holdings which have been successfully adjusted. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The holdings that could not be adjusted along with a reason for their failure. | [optional] 
**metadata** | **Dict[str, List[ResponseMetaData]]** | Contains warnings related to adjusted holdings | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.batch_adjust_holdings_response import BatchAdjustHoldingsResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist

values: Optional[Dict[str, HoldingAdjustmentWithDate]] = # Replace with your value
failed: Optional[Dict[str, ErrorDetail]] = # Replace with your value
metadata: Optional[Dict[str, conlist(ResponseMetaData)]] = # Replace with your value
links: Optional[conlist(Link)] = None
batch_adjust_holdings_response_instance = BatchAdjustHoldingsResponse(values=values, failed=failed, metadata=metadata, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

