# UpdateTaxRuleSetRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | 
**description** | **str** |  | 
**rules** | [**List[TaxRule]**](TaxRule.md) |  | 

## Example

```python
from lusid.models.update_tax_rule_set_request import UpdateTaxRuleSetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTaxRuleSetRequest from a JSON string
update_tax_rule_set_request_instance = UpdateTaxRuleSetRequest.from_json(json)
# print the JSON string representation of the object
print UpdateTaxRuleSetRequest.to_json()

# convert the object into a dict
update_tax_rule_set_request_dict = update_tax_rule_set_request_instance.to_dict()
# create an instance of UpdateTaxRuleSetRequest from a dict
update_tax_rule_set_request_form_dict = update_tax_rule_set_request.from_dict(update_tax_rule_set_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


