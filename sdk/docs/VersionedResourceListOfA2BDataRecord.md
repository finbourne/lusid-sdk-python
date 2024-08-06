# VersionedResourceListOfA2BDataRecord


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**Version**](Version.md) |  | 
**values** | [**List[A2BDataRecord]**](A2BDataRecord.md) |  | 
**href** | **str** |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.versioned_resource_list_of_a2_b_data_record import VersionedResourceListOfA2BDataRecord

# TODO update the JSON string below
json = "{}"
# create an instance of VersionedResourceListOfA2BDataRecord from a JSON string
versioned_resource_list_of_a2_b_data_record_instance = VersionedResourceListOfA2BDataRecord.from_json(json)
# print the JSON string representation of the object
print VersionedResourceListOfA2BDataRecord.to_json()

# convert the object into a dict
versioned_resource_list_of_a2_b_data_record_dict = versioned_resource_list_of_a2_b_data_record_instance.to_dict()
# create an instance of VersionedResourceListOfA2BDataRecord from a dict
versioned_resource_list_of_a2_b_data_record_form_dict = versioned_resource_list_of_a2_b_data_record.from_dict(versioned_resource_list_of_a2_b_data_record_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


