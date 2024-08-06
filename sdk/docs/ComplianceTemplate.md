# ComplianceTemplate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**description** | **str** | The description of the Compliance Template | 
**tags** | **List[str]** | Tags for a Compliance Template | [optional] 
**variations** | [**List[ComplianceTemplateVariation]**](ComplianceTemplateVariation.md) | Variation details of a Compliance Template | 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.compliance_template import ComplianceTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceTemplate from a JSON string
compliance_template_instance = ComplianceTemplate.from_json(json)
# print the JSON string representation of the object
print ComplianceTemplate.to_json()

# convert the object into a dict
compliance_template_dict = compliance_template_instance.to_dict()
# create an instance of ComplianceTemplate from a dict
compliance_template_form_dict = compliance_template.from_dict(compliance_template_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


