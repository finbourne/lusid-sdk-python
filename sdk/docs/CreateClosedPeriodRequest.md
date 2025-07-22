# CreateClosedPeriodRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**closed_period_id** | **str** | The unique Id of the Closed Period. The ClosedPeriodId, together with the Timeline Scope and Code, uniquely identifies a Closed Period | 
**effective_end** | **datetime** | The effective end of the Closed Period | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The Closed Periods properties. These will be from the &#39;ClosedPeriod&#39; domain. | [optional] 
**as_at_closed** | **datetime** | The asAt closed datetime for the Closed Period | [optional] 
**display_name** | **str** | The name of the Closed Period. | [optional] 
**description** | **str** | A description for the Closed Period. | [optional] 
## Example

```python
from lusid.models.create_closed_period_request import CreateClosedPeriodRequest
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr
from datetime import datetime
closed_period_id: StrictStr = "example_closed_period_id"
effective_end: Optional[datetime] = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
as_at_closed: Optional[datetime] = # Replace with your value
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
create_closed_period_request_instance = CreateClosedPeriodRequest(closed_period_id=closed_period_id, effective_end=effective_end, properties=properties, as_at_closed=as_at_closed, display_name=display_name, description=description)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

