# PagedResourceListOfPerson


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[Person]**](Person.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_person import PagedResourceListOfPerson

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfPerson from a JSON string
paged_resource_list_of_person_instance = PagedResourceListOfPerson.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfPerson.to_json()

# convert the object into a dict
paged_resource_list_of_person_dict = paged_resource_list_of_person_instance.to_dict()
# create an instance of PagedResourceListOfPerson from a dict
paged_resource_list_of_person_form_dict = paged_resource_list_of_person.from_dict(paged_resource_list_of_person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


