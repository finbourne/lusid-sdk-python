# PagedResourceListOfAbor


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[Abor]**](Abor.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_abor import PagedResourceListOfAbor

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfAbor from a JSON string
paged_resource_list_of_abor_instance = PagedResourceListOfAbor.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfAbor.to_json()

# convert the object into a dict
paged_resource_list_of_abor_dict = paged_resource_list_of_abor_instance.to_dict()
# create an instance of PagedResourceListOfAbor from a dict
paged_resource_list_of_abor_form_dict = paged_resource_list_of_abor.from_dict(paged_resource_list_of_abor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


