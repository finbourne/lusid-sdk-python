# CashAndSecurityOfferElection



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

## Example

```python
from lusid.models.cash_and_security_offer_election import CashAndSecurityOfferElection

# TODO update the JSON string below
json = "{}"
# create an instance of CashAndSecurityOfferElection from a JSON string
cash_and_security_offer_election_instance = CashAndSecurityOfferElection.from_json(json)
# print the JSON string representation of the object
print CashAndSecurityOfferElection.to_json()

# convert the object into a dict
cash_and_security_offer_election_dict = cash_and_security_offer_election_instance.to_dict()
# create an instance of CashAndSecurityOfferElection from a dict
cash_and_security_offer_election_form_dict = cash_and_security_offer_election.from_dict(cash_and_security_offer_election_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


