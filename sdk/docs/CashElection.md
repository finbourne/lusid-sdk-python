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

# TODO update the JSON string below
json = "{}"
# create an instance of CashElection from a JSON string
cash_election_instance = CashElection.from_json(json)
# print the JSON string representation of the object
print CashElection.to_json()

# convert the object into a dict
cash_election_dict = cash_election_instance.to_dict()
# create an instance of CashElection from a dict
cash_election_form_dict = cash_election.from_dict(cash_election_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


