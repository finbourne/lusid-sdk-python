# OrderFlowConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_entity_types** | **str** | Controls whether Orders and Allocations orders are included in the Portfolio valuation.  Valid values are None (to account for Transactions only), Allocations (to include Allocations and Transactions) and OrdersAndAllocations (to include Orders, Allocations and Transactions). | 
## Example

```python
from lusid.models.order_flow_configuration import OrderFlowConfiguration
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr

include_entity_types: StrictStr = "example_include_entity_types"
order_flow_configuration_instance = OrderFlowConfiguration(include_entity_types=include_entity_types)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

