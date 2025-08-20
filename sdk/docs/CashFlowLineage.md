# CashFlowLineage

Lineage for cash flow value
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_type** | **str** | The instrument type of the instrument to which the cash flow belongs to. When upserting CashFlowValues, this should be null. | [optional] 
**cash_flow_type** | **str** | The cashflow type.When upserting CashFlowValues, this should be null, or one of [Unknown, Coupon, Notional, Premium, Principal, Protection, Cash] | [optional] 
**instrument_id** | **str** | The LUID of the instrument to which the cash flow belongs to. When upserting this should be null. | [optional] 
**leg_id** | **str** | The leg id to which the cash flow belongs to. | [optional] 
**source_transaction_id** | **str** | The source transaction of the instrument to which the cash flow belongs to. When upserting this should be null | [optional] 
**pay_receive** | **str** | Does the cash flow belong to the Pay or Receive leg. When upserting this should either be null or one of [Pay, Receive, NotApplicable] | [optional] 
## Example

```python
from lusid.models.cash_flow_lineage import CashFlowLineage
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr

instrument_type: Optional[StrictStr] = "example_instrument_type"
cash_flow_type: Optional[StrictStr] = "example_cash_flow_type"
instrument_id: Optional[StrictStr] = "example_instrument_id"
leg_id: Optional[StrictStr] = "example_leg_id"
source_transaction_id: Optional[StrictStr] = "example_source_transaction_id"
pay_receive: Optional[StrictStr] = "example_pay_receive"
cash_flow_lineage_instance = CashFlowLineage(instrument_type=instrument_type, cash_flow_type=cash_flow_type, instrument_id=instrument_id, leg_id=leg_id, source_transaction_id=source_transaction_id, pay_receive=pay_receive)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

