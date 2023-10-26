# ComplianceRunInfoV2


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | [**ResourceId**](ResourceId.md) |  | 
**instigated_at** | **datetime** |  | 
**completed_at** | **datetime** |  | 
**schedule** | **str** |  | 
**instigated_by** | **str** |  | 

## Example

```python
from lusid.models.compliance_run_info_v2 import ComplianceRunInfoV2

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceRunInfoV2 from a JSON string
compliance_run_info_v2_instance = ComplianceRunInfoV2.from_json(json)
# print the JSON string representation of the object
print ComplianceRunInfoV2.to_json()

# convert the object into a dict
compliance_run_info_v2_dict = compliance_run_info_v2_instance.to_dict()
# create an instance of ComplianceRunInfoV2 from a dict
compliance_run_info_v2_form_dict = compliance_run_info_v2.from_dict(compliance_run_info_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


