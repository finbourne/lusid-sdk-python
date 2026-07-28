# ShareClassPnlBreakdown

The breakdown of PnL for a Share Class on a specified date.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apportioned_non_class_specific_pnl** | [**Dict[str, ShareClassAmount]**](ShareClassAmount.md) | Bucket of detail for PnL within the queried period not explicitly allocated to any share class but has been apportioned to the share class. | 
**class_pnl** | [**Dict[str, ShareClassAmount]**](ShareClassAmount.md) | Bucket of detail for PnL specific to the share class within the queried period. | 
**group_apportioned_pnl** | [**Dict[str, ShareClassAmount]**](ShareClassAmount.md) | Bucket of detail for the share class&#39;s apportioned share of PnL allocated to the allocation groups it belongs to, within the queried period. | 
**total_pnl** | [**Dict[str, ShareClassAmount]**](ShareClassAmount.md) | Bucket of detail for the total PnL within the queried period: the sum of the class-specific, apportioned non-class-specific and allocation-group-apportioned PnL. | 
## Example

```python
from lusid.models.share_class_pnl_breakdown import ShareClassPnlBreakdown
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

apportioned_non_class_specific_pnl: Dict[str, ShareClassAmount] = # Replace with your value
class_pnl: Dict[str, ShareClassAmount] = # Replace with your value
group_apportioned_pnl: Dict[str, ShareClassAmount] = # Replace with your value
total_pnl: Dict[str, ShareClassAmount] = # Replace with your value
share_class_pnl_breakdown_instance = ShareClassPnlBreakdown(apportioned_non_class_specific_pnl=apportioned_non_class_specific_pnl, class_pnl=class_pnl, group_apportioned_pnl=group_apportioned_pnl, total_pnl=total_pnl)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

