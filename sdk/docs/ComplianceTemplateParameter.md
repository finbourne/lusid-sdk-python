# ComplianceTemplateParameter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name for the required Compliance Template Parameter | 
**description** | **str** | The description for the required Compliance Template Parameter | 
**type** | **str** | The type for the required Compliance Template Parameter | 

## Example

```python
from lusid.models.compliance_template_parameter import ComplianceTemplateParameter

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceTemplateParameter from a JSON string
compliance_template_parameter_instance = ComplianceTemplateParameter.from_json(json)
# print the JSON string representation of the object
print ComplianceTemplateParameter.to_json()

# convert the object into a dict
compliance_template_parameter_dict = compliance_template_parameter_instance.to_dict()
# create an instance of ComplianceTemplateParameter from a dict
compliance_template_parameter_form_dict = compliance_template_parameter.from_dict(compliance_template_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


