# PortfolioCashLadder

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | The currency of the cash-flows. | 
**sub_holding_keys** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | The sub-holding properties which identify the holding. Each property will be from the &#39;Transaction&#39; domain. These are configured on a transaction portfolio. | [optional] 
**records** | [**List[CashLadderRecord]**](CashLadderRecord.md) | A record of cash flows on a specific date. | 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The records that could not be returned along with a reason for their failure. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.portfolio_cash_ladder import PortfolioCashLadder
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

currency: StrictStr = "example_currency"
sub_holding_keys: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
records: conlist(CashLadderRecord) = # Replace with your value
failed: Optional[Dict[str, ErrorDetail]] = # Replace with your value
links: Optional[conlist(Link)] = None
portfolio_cash_ladder_instance = PortfolioCashLadder(currency=currency, sub_holding_keys=sub_holding_keys, records=records, failed=failed, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

