# TenderOfferElection

Election for events that result in cash via a merger or acquisition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tender_offer_currency** | **str** | Currency of the cash offer | 
**tender_offer_price** | **float** | Price per share of the cash offer | 
**election_key** | **str** | Unique key associated to this election. | 
**is_chosen** | **bool** | Is this the election that has been explicitly chosen from multiple options. | [optional] 
**is_default** | **bool** | Is this election automatically applied in the absence of an election having been made.  May only be true for one election if multiple are provided. | [optional] 

## Example

```python
from lusid.models.tender_offer_election import TenderOfferElection

# TODO update the JSON string below
json = "{}"
# create an instance of TenderOfferElection from a JSON string
tender_offer_election_instance = TenderOfferElection.from_json(json)
# print the JSON string representation of the object
print TenderOfferElection.to_json()

# convert the object into a dict
tender_offer_election_dict = tender_offer_election_instance.to_dict()
# create an instance of TenderOfferElection from a dict
tender_offer_election_form_dict = tender_offer_election.from_dict(tender_offer_election_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


