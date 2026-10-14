# PartnerStatement

A partner's statement: the figures of their position on the fund over a period, fingerprinted so a later  statement can be compared against it.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statement_id** | **str** | The identifier of the statement. | 
**fund_id** | [**ResourceId**](ResourceId.md) |  | 
**investor_record_id** | **str** | The investor record the statement is for. | 
**period_start** | **datetime** | The start of the statement period, exclusive. | 
**period_end** | **datetime** | The end of the statement period, inclusive. | 
**nav_type_code** | **str** | The NAV type to produce the statement under. Defaults to the fund&#39;s primary NAV type. | 
**currency** | **str** | The currency of the statement. | 
**lines** | [**List[PartnerStatementLine]**](PartnerStatementLine.md) | The figures on the statement. | 
**fingerprint** | **str** | A hash of the statement&#39;s content, so two statements can be told apart. | 
**produced_as_at** | **datetime** | When the statement was produced. | 
## Example

```python
from lusid.models.partner_statement import PartnerStatement
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

statement_id: StrictStr = "example_statement_id"
fund_id: ResourceId = # Replace with your value
investor_record_id: StrictStr = "example_investor_record_id"
period_start: datetime = # Replace with your value
period_end: datetime = # Replace with your value
nav_type_code: StrictStr = "example_nav_type_code"
currency: StrictStr = "example_currency"
lines: List[PartnerStatementLine] = # Replace with your value
fingerprint: StrictStr = "example_fingerprint"
produced_as_at: datetime = # Replace with your value
partner_statement_instance = PartnerStatement(statement_id=statement_id, fund_id=fund_id, investor_record_id=investor_record_id, period_start=period_start, period_end=period_end, nav_type_code=nav_type_code, currency=currency, lines=lines, fingerprint=fingerprint, produced_as_at=produced_as_at)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

