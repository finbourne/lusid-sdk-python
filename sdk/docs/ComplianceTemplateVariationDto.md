# ComplianceTemplateVariationDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | 
**description** | **str** |  | 
**outcome_description** | **str** |  | [optional] 
**referenced_group_label** | **str** |  | [optional] 
**steps** | [**List[ComplianceStep]**](ComplianceStep.md) |  | 

## Example

```python
from lusid.models.compliance_template_variation_dto import ComplianceTemplateVariationDto

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceTemplateVariationDto from a JSON string
compliance_template_variation_dto_instance = ComplianceTemplateVariationDto.from_json(json)
# print the JSON string representation of the object
print ComplianceTemplateVariationDto.to_json()

# convert the object into a dict
compliance_template_variation_dto_dict = compliance_template_variation_dto_instance.to_dict()
# create an instance of ComplianceTemplateVariationDto from a dict
compliance_template_variation_dto_form_dict = compliance_template_variation_dto.from_dict(compliance_template_variation_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


