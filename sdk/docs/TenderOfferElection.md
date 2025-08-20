# TenderOfferElection

Election for events that result in cash via a merger or acquisition
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tender_offer_currency** | **str** | Currency of the cash offer | 
**tender_offer_price** | **float** | Price per share of the cash offer | 
**election_key** | **str** | Unique key associated to this election. | 
**is_chosen** | **bool** | Is this the election that has been explicitly chosen from multiple options. | [optional] 
**is_default** | **bool** | Is this election automatically applied in the absence of an election having been made. May only be true for one election if multiple are provided. | [optional] 
## Example

```python
from lusid.models.tender_offer_election import TenderOfferElection
from typing import Any, Dict, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, constr

tender_offer_currency: StrictStr = "example_tender_offer_currency"
tender_offer_price: Union[StrictFloat, StrictInt] = # Replace with your value
election_key: StrictStr = "example_election_key"
is_chosen: Optional[StrictBool] = # Replace with your value
is_chosen:Optional[StrictBool] = None
is_default: Optional[StrictBool] = # Replace with your value
is_default:Optional[StrictBool] = None
tender_offer_election_instance = TenderOfferElection(tender_offer_currency=tender_offer_currency, tender_offer_price=tender_offer_price, election_key=election_key, is_chosen=is_chosen, is_default=is_default)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

