# ShareClassPnlBreakdown

The breakdown of PnL for a Share Class on a specified date.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apportioned_non_class_specific_pnl** | [**Dict[str, ShareClassAmount]**](ShareClassAmount.md) | Bucket of detail for PnL within the queried period not explicitly allocated to any share class but has been apportioned to the share class. | 
**class_pnl** | [**Dict[str, ShareClassAmount]**](ShareClassAmount.md) | Bucket of detail for PnL specific to the share class within the queried period. | 
**total_pnl** | [**Dict[str, ShareClassAmount]**](ShareClassAmount.md) | Bucket of detail for the sum of class PnL and PnL not specific to a class within the queried period. | 
## Example

```python
from lusid.models.share_class_pnl_breakdown import ShareClassPnlBreakdown
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field

apportioned_non_class_specific_pnl: Dict[str, ShareClassAmount] = # Replace with your value
class_pnl: Dict[str, ShareClassAmount] = # Replace with your value
total_pnl: Dict[str, ShareClassAmount] = # Replace with your value
share_class_pnl_breakdown_instance = ShareClassPnlBreakdown(apportioned_non_class_specific_pnl=apportioned_non_class_specific_pnl, class_pnl=class_pnl, total_pnl=total_pnl)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

