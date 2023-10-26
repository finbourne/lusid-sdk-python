# ResourceListOfComplianceRunInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[ComplianceRunInfo]**](ComplianceRunInfo.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_compliance_run_info import ResourceListOfComplianceRunInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfComplianceRunInfo from a JSON string
resource_list_of_compliance_run_info_instance = ResourceListOfComplianceRunInfo.from_json(json)
# print the JSON string representation of the object
print ResourceListOfComplianceRunInfo.to_json()

# convert the object into a dict
resource_list_of_compliance_run_info_dict = resource_list_of_compliance_run_info_instance.to_dict()
# create an instance of ResourceListOfComplianceRunInfo from a dict
resource_list_of_compliance_run_info_form_dict = resource_list_of_compliance_run_info.from_dict(resource_list_of_compliance_run_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


