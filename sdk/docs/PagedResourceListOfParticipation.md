# PagedResourceListOfParticipation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[Participation]**](Participation.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_participation import PagedResourceListOfParticipation

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfParticipation from a JSON string
paged_resource_list_of_participation_instance = PagedResourceListOfParticipation.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfParticipation.to_json()

# convert the object into a dict
paged_resource_list_of_participation_dict = paged_resource_list_of_participation_instance.to_dict()
# create an instance of PagedResourceListOfParticipation from a dict
paged_resource_list_of_participation_form_dict = paged_resource_list_of_participation.from_dict(paged_resource_list_of_participation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


