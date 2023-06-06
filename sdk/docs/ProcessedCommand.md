# ProcessedCommand

The list of commands.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the command issued. | 
**path** | **str** | The unique identifier for the command including the request id. | [optional] 
**user_id** | [**User**](User.md) |  | 
**processed_time** | **datetime** | The asAt datetime that the events published by the processing of this command were committed to LUSID. | 

## Example

```python
from lusid.models.processed_command import ProcessedCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessedCommand from a JSON string
processed_command_instance = ProcessedCommand.from_json(json)
# print the JSON string representation of the object
print ProcessedCommand.to_json()

# convert the object into a dict
processed_command_dict = processed_command_instance.to_dict()
# create an instance of ProcessedCommand from a dict
processed_command_form_dict = processed_command.from_dict(processed_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


