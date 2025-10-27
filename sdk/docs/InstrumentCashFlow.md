# InstrumentCashFlow

The details for the cashflow associated with an instrument from a given portfolio.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_date** | **datetime** | The date at which the given cash flow is due to be paid (SettlementDate is used somewhat interchangeably with PaymentDate.) | 
**amount** | **float** | The quantity (amount) that will be paid. Note that this can be empty if the payment is in the future and a model is used that cannot estimate it. | [optional] 
**currency** | **str** | The payment currency of the cash flow. | 
**source_portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**source_transaction_id** | **str** | The identifier for the parent transaction on the instrument that will pay/receive this cash flow. | 
**source_instrument_scope** | **str** | The unique Lusid Instrument Id (LUID) of the instrument that the holding is in. | 
**source_instrument_id** | **str** | The unique Lusid Instrument Id (LUID) of the instrument that the holding is in. | 
**diagnostics** | **Dict[str, Optional[str]]** | Whilst a cash flow is defined by an (amount,ccy) pair and the date it is paid on there is additional information required for diagnostics. This includes a range of information and can be empty in the case of a simple cash quantity or where further information is not available. Typical information includes items such as reset dates, RIC, accrual start/end, number of days and curve data. | 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.instrument_cash_flow import InstrumentCashFlow
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

payment_date: datetime = # Replace with your value
amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
currency: StrictStr = "example_currency"
source_portfolio_id: ResourceId = # Replace with your value
source_transaction_id: StrictStr = "example_source_transaction_id"
source_instrument_scope: StrictStr = "example_source_instrument_scope"
source_instrument_id: StrictStr = "example_source_instrument_id"
diagnostics: Dict[str, Optional[StrictStr]] = # Replace with your value
links: Optional[List[Link]] = None
instrument_cash_flow_instance = InstrumentCashFlow(payment_date=payment_date, amount=amount, currency=currency, source_portfolio_id=source_portfolio_id, source_transaction_id=source_transaction_id, source_instrument_scope=source_instrument_scope, source_instrument_id=source_instrument_id, diagnostics=diagnostics, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

