# CreateAmortisationRuleSetRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**display_name** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from lusid.models.create_amortisation_rule_set_request import CreateAmortisationRuleSetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAmortisationRuleSetRequest from a JSON string
create_amortisation_rule_set_request_instance = CreateAmortisationRuleSetRequest.from_json(json)
# print the JSON string representation of the object
print CreateAmortisationRuleSetRequest.to_json()

# convert the object into a dict
create_amortisation_rule_set_request_dict = create_amortisation_rule_set_request_instance.to_dict()
# create an instance of CreateAmortisationRuleSetRequest from a dict
create_amortisation_rule_set_request_form_dict = create_amortisation_rule_set_request.from_dict(create_amortisation_rule_set_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


