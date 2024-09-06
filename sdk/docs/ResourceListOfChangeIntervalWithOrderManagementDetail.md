# ResourceListOfChangeIntervalWithOrderManagementDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[ChangeIntervalWithOrderManagementDetail]**](ChangeIntervalWithOrderManagementDetail.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_change_interval_with_order_management_detail import ResourceListOfChangeIntervalWithOrderManagementDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfChangeIntervalWithOrderManagementDetail from a JSON string
resource_list_of_change_interval_with_order_management_detail_instance = ResourceListOfChangeIntervalWithOrderManagementDetail.from_json(json)
# print the JSON string representation of the object
print ResourceListOfChangeIntervalWithOrderManagementDetail.to_json()

# convert the object into a dict
resource_list_of_change_interval_with_order_management_detail_dict = resource_list_of_change_interval_with_order_management_detail_instance.to_dict()
# create an instance of ResourceListOfChangeIntervalWithOrderManagementDetail from a dict
resource_list_of_change_interval_with_order_management_detail_form_dict = resource_list_of_change_interval_with_order_management_detail.from_dict(resource_list_of_change_interval_with_order_management_detail_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


