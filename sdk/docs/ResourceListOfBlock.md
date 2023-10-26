# ResourceListOfBlock


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[Block]**](Block.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_block import ResourceListOfBlock

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfBlock from a JSON string
resource_list_of_block_instance = ResourceListOfBlock.from_json(json)
# print the JSON string representation of the object
print ResourceListOfBlock.to_json()

# convert the object into a dict
resource_list_of_block_dict = resource_list_of_block_instance.to_dict()
# create an instance of ResourceListOfBlock from a dict
resource_list_of_block_form_dict = resource_list_of_block.from_dict(resource_list_of_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


