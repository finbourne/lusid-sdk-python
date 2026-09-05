# HoldingPropertyDelta

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**holding_property_key** | **str** | The running balance on the holding to adjust. Allowed values: &#39;CommittedCapital&#39;, &#39;FundedCapital&#39;, &#39;UnfundedCapital&#39;, &#39;RecallableCapital&#39; and &#39;NonRecallableCapital&#39;. Available values: CommittedCapital, FundedCapital, UnfundedCapital, RecallableCapital, NonRecallableCapital. | 
**source** | **str** | The movement value that sources the adjustment. Allowed values: &#39;Amount&#39; (the movement&#39;s signed amount in transaction currency), &#39;Units&#39; (the movement&#39;s signed units) and &#39;PortfolioAmount&#39; (the movement&#39;s signed amount converted to portfolio currency). Available values: Amount, Units, PortfolioAmount. | 
**direction** | **str** | Whether the sourced value increases or decreases the balance. Allowed values: &#39;Increase&#39; and &#39;Decrease&#39;. Available values: Increase, Decrease. | 
## Example

```python
from lusid.models.holding_property_delta import HoldingPropertyDelta
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

holding_property_key: StrictStr = "example_holding_property_key"
source: StrictStr = "example_source"
direction: StrictStr = "example_direction"
holding_property_delta_instance = HoldingPropertyDelta(holding_property_key=holding_property_key, source=source, direction=direction)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

