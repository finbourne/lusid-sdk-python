# CreateComplianceTemplateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code given for the Compliance Template | 
**description** | **str** | The description of the Compliance Template | 
**variations** | [**List[ComplianceTemplateVariationRequest]**](ComplianceTemplateVariationRequest.md) | Variation details of a Compliance Template | 

## Example

```python
from lusid.models.create_compliance_template_request import CreateComplianceTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateComplianceTemplateRequest from a JSON string
create_compliance_template_request_instance = CreateComplianceTemplateRequest.from_json(json)
# print the JSON string representation of the object
print CreateComplianceTemplateRequest.to_json()

# convert the object into a dict
create_compliance_template_request_dict = create_compliance_template_request_instance.to_dict()
# create an instance of CreateComplianceTemplateRequest from a dict
create_compliance_template_request_form_dict = create_compliance_template_request.from_dict(create_compliance_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


