# UpdateComplianceTemplateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code given for the Compliance Template | 
**description** | **str** | The description of the Compliance Template | 
**variations** | [**List[ComplianceTemplateVariationRequest]**](ComplianceTemplateVariationRequest.md) | Variation details of a Compliance Template | 

## Example

```python
from lusid.models.update_compliance_template_request import UpdateComplianceTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateComplianceTemplateRequest from a JSON string
update_compliance_template_request_instance = UpdateComplianceTemplateRequest.from_json(json)
# print the JSON string representation of the object
print UpdateComplianceTemplateRequest.to_json()

# convert the object into a dict
update_compliance_template_request_dict = update_compliance_template_request_instance.to_dict()
# create an instance of UpdateComplianceTemplateRequest from a dict
update_compliance_template_request_form_dict = update_compliance_template_request.from_dict(update_compliance_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


