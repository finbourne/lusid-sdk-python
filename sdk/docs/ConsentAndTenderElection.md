# ConsentAndTenderElection

Election to both grant consent and tender the holding (CTEN), optionally for a tender offer price and consent fee.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**election_key** | **str** | Unique key associated to this election. | 
**is_default** | **bool** | Is this election automatically applied in the absence of an election having been made.  May only be true for one election if multiple are provided. | [optional] 
**is_chosen** | **bool** | Is this the election that has been explicitly chosen from multiple options. | [optional] 
**tender_offer_price** | **float** | Optional. Price per unit offered for the tendered holding. | [optional] 
**tender_offer_currency** | **str** | Optional. Currency of the tender offer. Required if a tender offer price is provided. | [optional] 
**consent_fee_price** | **float** | Optional. The consent fee paid per unit for granting consent. | [optional] 
**consent_fee_currency** | **str** | Optional. Currency of the consent fee. Required if a consent fee price is provided. | [optional] 
## Example

```python
from lusid.models.consent_and_tender_election import ConsentAndTenderElection
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

election_key: StrictStr = "example_election_key"
is_default: Optional[StrictBool] = # Replace with your value
is_default:Optional[StrictBool] = None
is_chosen: Optional[StrictBool] = # Replace with your value
is_chosen:Optional[StrictBool] = None
tender_offer_price: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
tender_offer_currency: Optional[StrictStr] = "example_tender_offer_currency"
consent_fee_price: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
consent_fee_currency: Optional[StrictStr] = "example_consent_fee_currency"
consent_and_tender_election_instance = ConsentAndTenderElection(election_key=election_key, is_default=is_default, is_chosen=is_chosen, tender_offer_price=tender_offer_price, tender_offer_currency=tender_offer_currency, consent_fee_price=consent_fee_price, consent_fee_currency=consent_fee_currency)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

