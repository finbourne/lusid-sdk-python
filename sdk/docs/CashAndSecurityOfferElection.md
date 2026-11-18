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
**is_default** | **bool** | Is this election automatically applied in the absence of an election having been made.  May only be true for one election if multiple are provided. | [optional] 
**units_ratio** | [**UnitsRatio**](UnitsRatio.md) |  | 
**consent_fee_price** | **float** | Optional. The consent fee paid to holders who consent, on top of the exchange consideration. Quoted per 1,000 of face for bonds, using the current notional at the effective date of the event, and per unit for other instruments. Must be greater than 0. Required together with ConsentFeeCurrency, and only supported on an ExchangeOfferEvent. | [optional] 
**consent_fee_currency** | **str** | Optional. Currency of the consent fee. Required if a consent fee price is provided, and only supported on an ExchangeOfferEvent. | [optional] 
## Example

```python
from lusid.models.cash_and_security_offer_election import CashAndSecurityOfferElection
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

cash_offer_currency: StrictStr = "example_cash_offer_currency"
cash_offer_price: Union[StrictFloat, StrictInt] = # Replace with your value
cost_factor: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
election_key: StrictStr = "example_election_key"
is_chosen: Optional[StrictBool] = # Replace with your value
is_chosen:Optional[StrictBool] = None
is_default: Optional[StrictBool] = # Replace with your value
is_default:Optional[StrictBool] = None
units_ratio: UnitsRatio = # Replace with your value
consent_fee_price: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
consent_fee_currency: Optional[StrictStr] = "example_consent_fee_currency"
cash_and_security_offer_election_instance = CashAndSecurityOfferElection(cash_offer_currency=cash_offer_currency, cash_offer_price=cash_offer_price, cost_factor=cost_factor, election_key=election_key, is_chosen=is_chosen, is_default=is_default, units_ratio=units_ratio, consent_fee_price=consent_fee_price, consent_fee_currency=consent_fee_currency)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

