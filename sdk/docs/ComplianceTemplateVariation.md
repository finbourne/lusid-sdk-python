# ComplianceTemplateVariation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Label of a Compliance Template Variation | 
**description** | **str** | The description of the Compliance Template Variation | 
**required_parameters** | [**List[ComplianceTemplateParameter]**](ComplianceTemplateParameter.md) | A parameter required by a Compliance Template Variation | 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Properties associated with the Compliance Template Variation | 
**accepted_address_keys** | [**ResourceId**](ResourceId.md) |  | 
**steps** | [**List[ComplianceStep]**](ComplianceStep.md) | The steps expressed in this template, with their required parameters | 
**referenced_group_label** | **str** | The label of a given referenced group in a Compliance Rule Template Variation | [optional] 

## Example

```python
from lusid.models.compliance_template_variation import ComplianceTemplateVariation

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceTemplateVariation from a JSON string
compliance_template_variation_instance = ComplianceTemplateVariation.from_json(json)
# print the JSON string representation of the object
print ComplianceTemplateVariation.to_json()

# convert the object into a dict
compliance_template_variation_dict = compliance_template_variation_instance.to_dict()
# create an instance of ComplianceTemplateVariation from a dict
compliance_template_variation_form_dict = compliance_template_variation.from_dict(compliance_template_variation_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


