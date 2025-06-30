# HoldingsAdjustment

Full content of a holdings adjustment for a single portfolio and effective date.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_at** | **datetime** | The effective datetime from which the adjustment is valid. There can only be one holdings adjustment for a transaction portfolio at a specific effective datetime, so this uniquely identifies the adjustment. | 
**version** | [**Version**](Version.md) |  | 
**unmatched_holding_method** | **str** | Describes how the holdings were adjusted. If &#39;PositionToZero&#39; the entire transaction portfolio&#39;s holdings were set via a call to &#39;Set holdings&#39;. If &#39;KeepTheSame&#39; only the specified holdings were adjusted via a call to &#39;Adjust holdings&#39;. The available values are: PositionToZero, KeepTheSame | 
**adjustments** | [**List[HoldingAdjustment]**](HoldingAdjustment.md) | The holding adjustments. | 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.holdings_adjustment import HoldingsAdjustment
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, validator
from datetime import datetime
effective_at: datetime = # Replace with your value
version: Version = # Replace with your value
unmatched_holding_method: StrictStr = "example_unmatched_holding_method"
adjustments: conlist(HoldingAdjustment) = # Replace with your value
links: Optional[conlist(Link)] = None
holdings_adjustment_instance = HoldingsAdjustment(effective_at=effective_at, version=version, unmatched_holding_method=unmatched_holding_method, adjustments=adjustments, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

