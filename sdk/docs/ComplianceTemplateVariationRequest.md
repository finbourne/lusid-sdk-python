# ComplianceTemplateVariationRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | 
**description** | **str** |  | 
**outcome_description** | **str** |  | [optional] 
**referenced_group_label** | **str** |  | [optional] 
**steps** | [**List[ComplianceStepRequest]**](ComplianceStepRequest.md) |  | 

## Example

```python
from lusid.models.compliance_template_variation_request import ComplianceTemplateVariationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceTemplateVariationRequest from a JSON string
compliance_template_variation_request_instance = ComplianceTemplateVariationRequest.from_json(json)
# print the JSON string representation of the object
print ComplianceTemplateVariationRequest.to_json()

# convert the object into a dict
compliance_template_variation_request_dict = compliance_template_variation_request_instance.to_dict()
# create an instance of ComplianceTemplateVariationRequest from a dict
compliance_template_variation_request_form_dict = compliance_template_variation_request.from_dict(compliance_template_variation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


