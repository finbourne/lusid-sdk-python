# CashOfferElection

CashOfferElection for events for merger events resulting in cash

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cash_offer_currency** | **str** | Currency of the cash offer | 
**cash_offer_price** | **float** | Price per share of the cash offer | 
**election_key** | **str** | Unique key associated to this election. | 
**is_chosen** | **bool** | Is this the election that has been explicitly chosen from multiple options. | [optional] 
**is_default** | **bool** | Is this election automatically applied in the absence of an election having been made.  May only be true for one election if multiple are provided. | [optional] 

## Example

```python
from lusid.models.cash_offer_election import CashOfferElection

# TODO update the JSON string below
json = "{}"
# create an instance of CashOfferElection from a JSON string
cash_offer_election_instance = CashOfferElection.from_json(json)
# print the JSON string representation of the object
print CashOfferElection.to_json()

# convert the object into a dict
cash_offer_election_dict = cash_offer_election_instance.to_dict()
# create an instance of CashOfferElection from a dict
cash_offer_election_form_dict = cash_offer_election.from_dict(cash_offer_election_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


