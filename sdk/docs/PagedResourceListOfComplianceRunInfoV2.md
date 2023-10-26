# PagedResourceListOfComplianceRunInfoV2


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[ComplianceRunInfoV2]**](ComplianceRunInfoV2.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_compliance_run_info_v2 import PagedResourceListOfComplianceRunInfoV2

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfComplianceRunInfoV2 from a JSON string
paged_resource_list_of_compliance_run_info_v2_instance = PagedResourceListOfComplianceRunInfoV2.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfComplianceRunInfoV2.to_json()

# convert the object into a dict
paged_resource_list_of_compliance_run_info_v2_dict = paged_resource_list_of_compliance_run_info_v2_instance.to_dict()
# create an instance of PagedResourceListOfComplianceRunInfoV2 from a dict
paged_resource_list_of_compliance_run_info_v2_form_dict = paged_resource_list_of_compliance_run_info_v2.from_dict(paged_resource_list_of_compliance_run_info_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


