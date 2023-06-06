# ResourceListOfProcessedCommand


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[ProcessedCommand]**](ProcessedCommand.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_processed_command import ResourceListOfProcessedCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfProcessedCommand from a JSON string
resource_list_of_processed_command_instance = ResourceListOfProcessedCommand.from_json(json)
# print the JSON string representation of the object
print ResourceListOfProcessedCommand.to_json()

# convert the object into a dict
resource_list_of_processed_command_dict = resource_list_of_processed_command_instance.to_dict()
# create an instance of ResourceListOfProcessedCommand from a dict
resource_list_of_processed_command_form_dict = resource_list_of_processed_command.from_dict(resource_list_of_processed_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


