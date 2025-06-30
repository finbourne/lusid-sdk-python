# OrderBreachHistory

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**order_id** | [**ResourceId**](ResourceId.md) |  | 
**run_id** | [**ResourceId**](ResourceId.md) |  | 
**breaches_by_rule** | **Dict[str, List[OrderRuleBreach]]** | Compliance rule breaches associations with the order and run. | [optional] 
**as_at** | **datetime** | The asAt datetime at which the order breach was created in LUSID. | 
## Example

```python
from lusid.models.order_breach_history import OrderBreachHistory
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist
from datetime import datetime
id: ResourceId = # Replace with your value
order_id: ResourceId = # Replace with your value
run_id: ResourceId = # Replace with your value
breaches_by_rule: Optional[Dict[str, conlist(OrderRuleBreach)]] = # Replace with your value
as_at: datetime = # Replace with your value
order_breach_history_instance = OrderBreachHistory(id=id, order_id=order_id, run_id=run_id, breaches_by_rule=breaches_by_rule, as_at=as_at)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

