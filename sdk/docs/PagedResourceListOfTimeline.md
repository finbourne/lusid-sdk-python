# PagedResourceListOfTimeline


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[Timeline]**](Timeline.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_timeline import PagedResourceListOfTimeline

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfTimeline from a JSON string
paged_resource_list_of_timeline_instance = PagedResourceListOfTimeline.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfTimeline.to_json()

# convert the object into a dict
paged_resource_list_of_timeline_dict = paged_resource_list_of_timeline_instance.to_dict()
# create an instance of PagedResourceListOfTimeline from a dict
paged_resource_list_of_timeline_form_dict = paged_resource_list_of_timeline.from_dict(paged_resource_list_of_timeline_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


