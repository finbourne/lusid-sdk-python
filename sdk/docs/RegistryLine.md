# RegistryLine

A line of a portfolio's registry: a partner register line with the fields of a holding row and its capital  balances. Registry lines are never holdings, so a line here is absent from the portfolio's holdings.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**instrument_scope** | **str** | The scope in which the line&#39;s capital-interest instrument is in. | [optional] 
**instrument_uid** | **str** | The unique Lusid Instrument Id (LUID) of the capital-interest instrument of the line. | 
**sub_holding_keys** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | The sub-holding properties which identify the holding. Each property will be from the &#39;Transaction&#39; domain. These are configured on a transaction portfolio. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The properties which have been requested to be decorated onto the line. These will be from the &#39;Instrument&#39; or &#39;Holding&#39; domain; the capital balances are available as &#39;Holding/system&#39; properties when requested by key. | [optional] 
**holding_type** | **str** | The code for the type of the holding e.g. P, B, C, R, F etc. | 
**holding_type_name** | **str** | The decoded type of the holding e.g. Position, Balance, CashCommitment, Receivable, ForwardFX etc. | [optional] 
**units** | **float** | The number of units of the line, one per open line. | 
**settled_units** | **float** | The number of settled units of the line. | 
**cost** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**cost_portfolio_ccy** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**currency** | **str** | The commitment currency of the line. | [optional] 
**holding_id** | **int** | A single identifier for the line within the portfolio, constructed from the LusidInstrumentId, sub-holding keys and currency. | [optional] 
**investor_record_id** | **str** | The identifier of the investor record the line belongs to, as the register shows it. | 
**commitment_line_id** | **str** | The identifier of the commitment (register) line, as its capital-interest instrument declares it. | 
**committed** | **float** | The committed capital, in the commitment currency. | 
**uncalled_commitment** | **float** | The commitment not yet called, in the commitment currency. | 
**paid_in** | **float** | The capital paid in, in the commitment currency. | 
**returned** | **float** | The capital returned, in the commitment currency. | 
**recallable** | **float** | The returned capital that may be recalled, in the commitment currency. | 
**unfunded** | **float** | The unfunded commitment: the uncalled commitment plus the recallable capital, in the commitment currency. | 
## Example

```python
from lusid.models.registry_line import RegistryLine
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

portfolio_id: ResourceId = # Replace with your value
instrument_scope: Optional[StrictStr] = "example_instrument_scope"
instrument_uid: StrictStr = "example_instrument_uid"
sub_holding_keys: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
holding_type: StrictStr = "example_holding_type"
holding_type_name: Optional[StrictStr] = "example_holding_type_name"
units: Union[StrictFloat, StrictInt] = # Replace with your value
settled_units: Union[StrictFloat, StrictInt] = # Replace with your value
cost: CurrencyAndAmount
cost_portfolio_ccy: CurrencyAndAmount = # Replace with your value
currency: Optional[StrictStr] = "example_currency"
holding_id: Optional[StrictInt] = # Replace with your value
investor_record_id: StrictStr = "example_investor_record_id"
commitment_line_id: StrictStr = "example_commitment_line_id"
committed: Union[StrictFloat, StrictInt] = # Replace with your value
uncalled_commitment: Union[StrictFloat, StrictInt] = # Replace with your value
paid_in: Union[StrictFloat, StrictInt] = # Replace with your value
returned: Union[StrictFloat, StrictInt] = # Replace with your value
recallable: Union[StrictFloat, StrictInt] = # Replace with your value
unfunded: Union[StrictFloat, StrictInt] = # Replace with your value
registry_line_instance = RegistryLine(portfolio_id=portfolio_id, instrument_scope=instrument_scope, instrument_uid=instrument_uid, sub_holding_keys=sub_holding_keys, properties=properties, holding_type=holding_type, holding_type_name=holding_type_name, units=units, settled_units=settled_units, cost=cost, cost_portfolio_ccy=cost_portfolio_ccy, currency=currency, holding_id=holding_id, investor_record_id=investor_record_id, commitment_line_id=commitment_line_id, committed=committed, uncalled_commitment=uncalled_commitment, paid_in=paid_in, returned=returned, recallable=recallable, unfunded=unfunded)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

