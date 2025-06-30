# FundPnlBreakdown

The breakdown of PnL for a Fund on a specified date.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**non_class_specific_pnl** | [**Dict[str, FundAmount]**](FundAmount.md) | Bucket of detail for PnL within the queried period that is not specific to any share class. | 
**aggregated_class_pnl** | [**Dict[str, FundAmount]**](FundAmount.md) | Bucket of detail for the sum of class PnL across all share classes in a fund and within the queried period. | 
**total_pnl** | [**Dict[str, FundAmount]**](FundAmount.md) | Bucket of detail for the sum of class PnL and PnL not specific to a class within the queried period. | 
## Example

```python
from lusid.models.fund_pnl_breakdown import FundPnlBreakdown
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field

non_class_specific_pnl: Dict[str, FundAmount] = # Replace with your value
aggregated_class_pnl: Dict[str, FundAmount] = # Replace with your value
total_pnl: Dict[str, FundAmount] = # Replace with your value
fund_pnl_breakdown_instance = FundPnlBreakdown(non_class_specific_pnl=non_class_specific_pnl, aggregated_class_pnl=aggregated_class_pnl, total_pnl=total_pnl)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

