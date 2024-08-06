# ComplianceRule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** |  | 
**code** | **str** |  | 
**display_name** | **str** |  | 
**type** | **str** |  | 
**property_key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**address_key** | **str** |  | [optional] 
**lower_bound** | **float** |  | 
**upper_bound** | **float** |  | 
**schedule** | **str** |  | 
**hard_requirement** | **bool** |  | 
**target_portfolio_ids** | [**List[ResourceId]**](ResourceId.md) |  | 
**description** | **str** |  | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 

## Example

```python
from lusid.models.compliance_rule import ComplianceRule

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceRule from a JSON string
compliance_rule_instance = ComplianceRule.from_json(json)
# print the JSON string representation of the object
print ComplianceRule.to_json()

# convert the object into a dict
compliance_rule_dict = compliance_rule_instance.to_dict()
# create an instance of ComplianceRule from a dict
compliance_rule_form_dict = compliance_rule.from_dict(compliance_rule_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


