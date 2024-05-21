# SetAmortisationRulesRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rules_interval** | [**RulesInterval**](RulesInterval.md) |  | 

## Example

```python
from lusid.models.set_amortisation_rules_request import SetAmortisationRulesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetAmortisationRulesRequest from a JSON string
set_amortisation_rules_request_instance = SetAmortisationRulesRequest.from_json(json)
# print the JSON string representation of the object
print SetAmortisationRulesRequest.to_json()

# convert the object into a dict
set_amortisation_rules_request_dict = set_amortisation_rules_request_instance.to_dict()
# create an instance of SetAmortisationRulesRequest from a dict
set_amortisation_rules_request_form_dict = set_amortisation_rules_request.from_dict(set_amortisation_rules_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


