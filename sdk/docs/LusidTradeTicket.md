# LusidTradeTicket

A LUSID Trade Ticket comprising an instrument, a transaction, and a counterparty.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | Transaction ID. Must be unique. | 
**transaction_type** | **str** | Type of transaction for processing. Referenced by Transaction Configuration. | 
**source** | **str** | Transaction Source. Referenced by Transaction Configuration. | [optional] 
**transaction_date** | **str** | Transaction Date. Date at which transaction is known. | 
**settlement_date** | **str** | Transaction settlement. Date at which transaction is finalised and realised into the system. | 
**total_consideration** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**units** | **float** | Number of units in the transaction. For an OTC this is somewhat interchangeable with the quantity booked in the  instrument. As M x N or N x M are equivalent it is advised a client chooses one approach and sticks to it.  Arguably either the unit or holding is best unitised. | 
**instrument_identifiers** | **Dict[str, str]** | Identifiers for the instrument. | 
**instrument_scope** | **str** | Scope of instrument | [optional] 
**instrument_name** | **str** | Name of instrument | [optional] 
**instrument_definition** | [**LusidInstrument**](LusidInstrument.md) |  | [optional] 
**counterparty_agreement_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**counterparty** | **str** | Counterparty | [optional] 
**instrument_properties** | [**List[ModelProperty]**](ModelProperty.md) | Set of instrument properties (as defined by client/user). | [optional] 
**transaction_properties** | [**List[ModelProperty]**](ModelProperty.md) | Set of transaction properties (as defined by client/user). | [optional] 
**trade_ticket_type** | **str** | The available values are: LusidTradeTicket, ExternalTradeTicket | 
## Example

```python
from lusid.models.lusid_trade_ticket import LusidTradeTicket
from typing import Any, Dict, List, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist, constr, validator

transaction_id: StrictStr = "example_transaction_id"
transaction_type: StrictStr = "example_transaction_type"
source: Optional[StrictStr] = "example_source"
transaction_date: StrictStr = "example_transaction_date"
settlement_date: StrictStr = "example_settlement_date"
total_consideration: CurrencyAndAmount = # Replace with your value
units: Union[StrictFloat, StrictInt] = # Replace with your value
instrument_identifiers: Dict[str, StrictStr] = # Replace with your value
instrument_scope: Optional[StrictStr] = "example_instrument_scope"
instrument_name: Optional[StrictStr] = "example_instrument_name"
instrument_definition: Optional[LusidInstrument] = # Replace with your value
counterparty_agreement_id: Optional[ResourceId] = # Replace with your value
counterparty: Optional[StrictStr] = "example_counterparty"
instrument_properties: Optional[conlist(ModelProperty)] = # Replace with your value
transaction_properties: Optional[conlist(ModelProperty)] = # Replace with your value
trade_ticket_type: StrictStr = "example_trade_ticket_type"
lusid_trade_ticket_instance = LusidTradeTicket(transaction_id=transaction_id, transaction_type=transaction_type, source=source, transaction_date=transaction_date, settlement_date=settlement_date, total_consideration=total_consideration, units=units, instrument_identifiers=instrument_identifiers, instrument_scope=instrument_scope, instrument_name=instrument_name, instrument_definition=instrument_definition, counterparty_agreement_id=counterparty_agreement_id, counterparty=counterparty, instrument_properties=instrument_properties, transaction_properties=transaction_properties, trade_ticket_type=trade_ticket_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

