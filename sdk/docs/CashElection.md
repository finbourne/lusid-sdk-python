# CashElection

Cash election for Events that result in a cash payment.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**election_key** | **str** | Unique key used to identify this election. | 
**exchange_rate** | **float** | The exchange rate if this is not the declared CashElection.  Defaults to 1 if Election is Declared. | [optional] 
**dividend_rate** | **float** | The payment rate for this CashElection. | [optional] 
**is_chosen** | **bool** | Has this election been chosen.  Only one Election may be Chosen per Event. | [optional] 
**is_declared** | **bool** | Is this the declared CashElection.  Only one Election may be Declared per Event. | [optional] 
**is_default** | **bool** | Is this election the default.  Only one Election may be Default per Event | [optional] 
**dividend_currency** | **str** | The payment currency for this CashElection. | 
## Example

```python
from lusid.models.cash_election import CashElection
from typing import Any, Dict, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, constr

election_key: StrictStr = "example_election_key"
exchange_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
dividend_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
is_chosen: Optional[StrictBool] = # Replace with your value
is_chosen:Optional[StrictBool] = None
is_declared: Optional[StrictBool] = # Replace with your value
is_declared:Optional[StrictBool] = None
is_default: Optional[StrictBool] = # Replace with your value
is_default:Optional[StrictBool] = None
dividend_currency: StrictStr = "example_dividend_currency"
cash_election_instance = CashElection(election_key=election_key, exchange_rate=exchange_rate, dividend_rate=dividend_rate, is_chosen=is_chosen, is_declared=is_declared, is_default=is_default, dividend_currency=dividend_currency)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

