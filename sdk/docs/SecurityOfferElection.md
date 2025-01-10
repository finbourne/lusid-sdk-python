# SecurityOfferElection

Election for events that result in cash via a merger or acquisition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**election_key** | **str** | Unique key associated to this election. | 
**is_chosen** | **bool** | Is this the election that has been explicitly chosen from multiple options. | [optional] 
**is_default** | **bool** | Is this election automatically applied in the absence of an election having been made.  May only be true for one election if multiple are provided. | [optional] 
**units_ratio** | [**UnitsRatio**](UnitsRatio.md) |  | 

## Example

```python
from lusid.models.security_offer_election import SecurityOfferElection

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityOfferElection from a JSON string
security_offer_election_instance = SecurityOfferElection.from_json(json)
# print the JSON string representation of the object
print SecurityOfferElection.to_json()

# convert the object into a dict
security_offer_election_dict = security_offer_election_instance.to_dict()
# create an instance of SecurityOfferElection from a dict
security_offer_election_form_dict = security_offer_election.from_dict(security_offer_election_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


