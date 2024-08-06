# ResourceListOfTaxRuleSet


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[TaxRuleSet]**](TaxRuleSet.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_tax_rule_set import ResourceListOfTaxRuleSet

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfTaxRuleSet from a JSON string
resource_list_of_tax_rule_set_instance = ResourceListOfTaxRuleSet.from_json(json)
# print the JSON string representation of the object
print ResourceListOfTaxRuleSet.to_json()

# convert the object into a dict
resource_list_of_tax_rule_set_dict = resource_list_of_tax_rule_set_instance.to_dict()
# create an instance of ResourceListOfTaxRuleSet from a dict
resource_list_of_tax_rule_set_form_dict = resource_list_of_tax_rule_set.from_dict(resource_list_of_tax_rule_set_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


