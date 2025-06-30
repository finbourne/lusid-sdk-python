# OrderInstructionSetRequest

A request to create or update multiple OrderInstructions.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**List[OrderInstructionRequest]**](OrderInstructionRequest.md) | A collection of OrderInstructionRequests. | [optional] 
## Example

```python
from lusid.models.order_instruction_set_request import OrderInstructionSetRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist

requests: Optional[conlist(OrderInstructionRequest)] = # Replace with your value
order_instruction_set_request_instance = OrderInstructionSetRequest(requests=requests)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

