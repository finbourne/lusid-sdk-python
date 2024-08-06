# PagedResourceListOfDialectId


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[DialectId]**](DialectId.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_dialect_id import PagedResourceListOfDialectId

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfDialectId from a JSON string
paged_resource_list_of_dialect_id_instance = PagedResourceListOfDialectId.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfDialectId.to_json()

# convert the object into a dict
paged_resource_list_of_dialect_id_dict = paged_resource_list_of_dialect_id_instance.to_dict()
# create an instance of PagedResourceListOfDialectId from a dict
paged_resource_list_of_dialect_id_form_dict = paged_resource_list_of_dialect_id.from_dict(paged_resource_list_of_dialect_id_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


