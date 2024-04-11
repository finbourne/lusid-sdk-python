# UpdateAmortisationRuleSetDetailsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from lusid.models.update_amortisation_rule_set_details_request import UpdateAmortisationRuleSetDetailsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAmortisationRuleSetDetailsRequest from a JSON string
update_amortisation_rule_set_details_request_instance = UpdateAmortisationRuleSetDetailsRequest.from_json(json)
# print the JSON string representation of the object
print UpdateAmortisationRuleSetDetailsRequest.to_json()

# convert the object into a dict
update_amortisation_rule_set_details_request_dict = update_amortisation_rule_set_details_request_instance.to_dict()
# create an instance of UpdateAmortisationRuleSetDetailsRequest from a dict
update_amortisation_rule_set_details_request_form_dict = update_amortisation_rule_set_details_request.from_dict(update_amortisation_rule_set_details_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


