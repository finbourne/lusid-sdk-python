# PartnerCapitalAccount

A partner's capital account statement (PCAP) over a reporting period, in the ILPA row order, with quarter-,  year- and inception-to-date columns and a memo block of commitment balances from the register.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fund_id** | [**ResourceId**](ResourceId.md) |  | 
**investor_record_id** | **str** | The investor record identifier of the partner. | 
**currency** | **str** | The currency the capital account is expressed in, being the fund&#39;s base currency. | 
**period_start** | **datetime** | The exclusive start of the reporting period. | 
**period_end** | **datetime** | The inclusive end of the reporting period. | 
**status** | **str** | Whether the figures are an Estimate or Final. Figures are Final only once a valuation point covering the period end has been finalised. | 
**rows** | [**List[PartnerCapitalAccountRow]**](PartnerCapitalAccountRow.md) | The capital account rows, from beginning capital through to ending capital, each with quarter-to-date, year-to-date and inception-to-date columns. | 
**memo** | [**PartnerCapitalAccountMemo**](PartnerCapitalAccountMemo.md) |  | 
**foots** | **bool** | Whether the ending capital agrees across the quarter-to-date, year-to-date and inception-to-date columns within tolerance. | 
**footing_difference** | **float** | The largest difference between the ending capital of any two columns. | 
## Example

```python
from lusid.models.partner_capital_account import PartnerCapitalAccount
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

fund_id: ResourceId = # Replace with your value
investor_record_id: StrictStr = "example_investor_record_id"
currency: StrictStr = "example_currency"
period_start: datetime = # Replace with your value
period_end: datetime = # Replace with your value
status: StrictStr = "example_status"
rows: List[PartnerCapitalAccountRow] = # Replace with your value
memo: PartnerCapitalAccountMemo
foots: StrictBool = # Replace with your value
foots:StrictBool = True
footing_difference: Union[StrictFloat, StrictInt] = # Replace with your value
partner_capital_account_instance = PartnerCapitalAccount(fund_id=fund_id, investor_record_id=investor_record_id, currency=currency, period_start=period_start, period_end=period_end, status=status, rows=rows, memo=memo, foots=foots, footing_difference=footing_difference)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

