# PartnerCapitalAccountRowDetail

One labelled part of a capital account row's total: the kind of amount, the allocation event it arose on and its  quarter-, year- and inception-to-date amounts, each already included in the row's own column.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | The kind of amount the entry labels: WithholdingTax for tax withheld from a distribution on the partner&#39;s behalf. | 
**allocation_event_id** | [**ResourceId**](ResourceId.md) |  | 
**event_date** | **datetime** | The effective date of the allocation event the amount arose on. | 
**qtd** | **float** | The part of the row&#39;s quarter-to-date amount the entry labels; zero when the event falls outside the quarter. | 
**ytd** | **float** | The part of the row&#39;s year-to-date amount the entry labels; zero when the event falls outside the year. | 
**itd** | **float** | The part of the row&#39;s inception-to-date amount the entry labels. | 
## Example

```python
from lusid.models.partner_capital_account_row_detail import PartnerCapitalAccountRowDetail
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

kind: StrictStr = "example_kind"
allocation_event_id: ResourceId = # Replace with your value
event_date: datetime = # Replace with your value
qtd: Union[StrictFloat, StrictInt] = # Replace with your value
ytd: Union[StrictFloat, StrictInt] = # Replace with your value
itd: Union[StrictFloat, StrictInt] = # Replace with your value
partner_capital_account_row_detail_instance = PartnerCapitalAccountRowDetail(kind=kind, allocation_event_id=allocation_event_id, event_date=event_date, qtd=qtd, ytd=ytd, itd=itd)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

