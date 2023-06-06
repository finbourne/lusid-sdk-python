# PagedResourceListOfBlock


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[Block]**](Block.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_block import PagedResourceListOfBlock

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfBlock from a JSON string
paged_resource_list_of_block_instance = PagedResourceListOfBlock.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfBlock.to_json()

# convert the object into a dict
paged_resource_list_of_block_dict = paged_resource_list_of_block_instance.to_dict()
# create an instance of PagedResourceListOfBlock from a dict
paged_resource_list_of_block_form_dict = paged_resource_list_of_block.from_dict(paged_resource_list_of_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


