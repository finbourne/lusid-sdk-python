# LapseElection

Lapse election.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**election_key** | **str** | Unique key associated to this election | 
**is_default** | **bool** | Is this election automatically applied in the absence of an election having been made.  May only be true for one election if multiple are provided. | [optional] 
**is_chosen** | **bool** | Is this the election that has been explicitly chosen from multiple options. | [optional] 

## Example

```python
from lusid.models.lapse_election import LapseElection

# TODO update the JSON string below
json = "{}"
# create an instance of LapseElection from a JSON string
lapse_election_instance = LapseElection.from_json(json)
# print the JSON string representation of the object
print LapseElection.to_json()

# convert the object into a dict
lapse_election_dict = lapse_election_instance.to_dict()
# create an instance of LapseElection from a dict
lapse_election_form_dict = lapse_election.from_dict(lapse_election_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


