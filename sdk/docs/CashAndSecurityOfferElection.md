# CashAndSecurityOfferElection

Election for events that result in both cash and equity via a merger or acquisition
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cash_offer_currency** | **str** | Currency of the cash offer | 
**cash_offer_price** | **float** | Price per share of the cash offer | 
**cost_factor** | **float** | Optional. The fraction of cost that is transferred from the existing shares to the new shares. | [optional] 
**election_key** | **str** | Unique key associated to this election. | 
**is_chosen** | **bool** | Is this the election that has been explicitly chosen from multiple options. | [optional] 
**is_default** | **bool** | Is this election automatically applied in the absence of an election having been made. May only be true for one election if multiple are provided. | [optional] 
**units_ratio** | [**UnitsRatio**](UnitsRatio.md) |  | 
## Example

```python
from lusid.models.cash_and_security_offer_election import CashAndSecurityOfferElection
from typing import Any, Dict, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, constr

cash_offer_currency: StrictStr = "example_cash_offer_currency"
cash_offer_price: Union[StrictFloat, StrictInt] = # Replace with your value
cost_factor: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
election_key: StrictStr = "example_election_key"
is_chosen: Optional[StrictBool] = # Replace with your value
is_chosen:Optional[StrictBool] = None
is_default: Optional[StrictBool] = # Replace with your value
is_default:Optional[StrictBool] = None
units_ratio: UnitsRatio = # Replace with your value
cash_and_security_offer_election_instance = CashAndSecurityOfferElection(cash_offer_currency=cash_offer_currency, cash_offer_price=cash_offer_price, cost_factor=cost_factor, election_key=election_key, is_chosen=is_chosen, is_default=is_default, units_ratio=units_ratio)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

