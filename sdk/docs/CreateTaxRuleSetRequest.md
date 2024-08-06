# CreateTaxRuleSetRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** |  | 
**description** | **str** |  | 
**output_property_key** | **str** |  | 
**rules** | [**List[TaxRule]**](TaxRule.md) |  | 

## Example

```python
from lusid.models.create_tax_rule_set_request import CreateTaxRuleSetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTaxRuleSetRequest from a JSON string
create_tax_rule_set_request_instance = CreateTaxRuleSetRequest.from_json(json)
# print the JSON string representation of the object
print CreateTaxRuleSetRequest.to_json()

# convert the object into a dict
create_tax_rule_set_request_dict = create_tax_rule_set_request_instance.to_dict()
# create an instance of CreateTaxRuleSetRequest from a dict
create_tax_rule_set_request_form_dict = create_tax_rule_set_request.from_dict(create_tax_rule_set_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


