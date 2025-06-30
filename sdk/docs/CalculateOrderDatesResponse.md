# CalculateOrderDatesResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successes** | [**Dict[str, TransferAgencyDates]**](TransferAgencyDates.md) | A dictionary of successful date calculations, keyed by the request key. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | A dictionary of failed date calculations, keyed by the request key, containing the error details of any failures that occurred during the calculation. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.calculate_order_dates_response import CalculateOrderDatesResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist

successes: Optional[Dict[str, TransferAgencyDates]] = # Replace with your value
failed: Optional[Dict[str, ErrorDetail]] = # Replace with your value
links: Optional[conlist(Link)] = None
calculate_order_dates_response_instance = CalculateOrderDatesResponse(successes=successes, failed=failed, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

