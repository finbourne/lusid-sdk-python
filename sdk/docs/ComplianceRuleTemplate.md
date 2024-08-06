# ComplianceRuleTemplate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**description** | **str** | The description of the Compliance Template | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | Properties associated with the Compliance Template Variation | [optional] 
**variations** | [**List[ComplianceTemplateVariationDto]**](ComplianceTemplateVariationDto.md) | Variation details of a Compliance Template | [optional] 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested asAt datetime. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.compliance_rule_template import ComplianceRuleTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceRuleTemplate from a JSON string
compliance_rule_template_instance = ComplianceRuleTemplate.from_json(json)
# print the JSON string representation of the object
print ComplianceRuleTemplate.to_json()

# convert the object into a dict
compliance_rule_template_dict = compliance_rule_template_instance.to_dict()
# create an instance of ComplianceRuleTemplate from a dict
compliance_rule_template_form_dict = compliance_rule_template.from_dict(compliance_rule_template_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


