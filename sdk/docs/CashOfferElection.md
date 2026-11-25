# CashOfferElection

Election for events that result in cash via a merger or acquisition
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cash_offer_currency** | **str** | Currency of the cash offer | 
**cash_offer_price** | **float** | Price per share of the cash offer | 
**election_key** | **str** | Unique key associated to this election. | 
**is_chosen** | **bool** | Is this the election that has been explicitly chosen from multiple options. | [optional] 
**is_default** | **bool** | Is this election automatically applied in the absence of an election having been made.  May only be true for one election if multiple are provided. | [optional] 
**payment_date** | **datetime** | Optional. The date this option pays. On MergerEvent, RepurchaseOfferEvent, BonusIssueEvent and  ExchangeOfferEvent it sets the settlement date of this option&#39;s transactions; when omitted, the  event-level date applies. Not supported on other events. | [optional] 
## Example

```python
from lusid.models.cash_offer_election import CashOfferElection
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

cash_offer_currency: StrictStr = "example_cash_offer_currency"
cash_offer_price: Union[StrictFloat, StrictInt] = # Replace with your value
election_key: StrictStr = "example_election_key"
is_chosen: Optional[StrictBool] = # Replace with your value
is_chosen:Optional[StrictBool] = None
is_default: Optional[StrictBool] = # Replace with your value
is_default:Optional[StrictBool] = None
payment_date: Optional[datetime] = # Replace with your value
cash_offer_election_instance = CashOfferElection(cash_offer_currency=cash_offer_currency, cash_offer_price=cash_offer_price, election_key=election_key, is_chosen=is_chosen, is_default=is_default, payment_date=payment_date)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

