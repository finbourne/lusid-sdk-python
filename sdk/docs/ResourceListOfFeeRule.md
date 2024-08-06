# ResourceListOfFeeRule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[FeeRule]**](FeeRule.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_fee_rule import ResourceListOfFeeRule

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfFeeRule from a JSON string
resource_list_of_fee_rule_instance = ResourceListOfFeeRule.from_json(json)
# print the JSON string representation of the object
print ResourceListOfFeeRule.to_json()

# convert the object into a dict
resource_list_of_fee_rule_dict = resource_list_of_fee_rule_instance.to_dict()
# create an instance of ResourceListOfFeeRule from a dict
resource_list_of_fee_rule_form_dict = resource_list_of_fee_rule.from_dict(resource_list_of_fee_rule_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


