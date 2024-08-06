# SequenceDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**increment** | **int** | The Resource Id of the sequence definition | 
**min_value** | **int** | The minimum value of the sequence | 
**max_value** | **int** | The maximum value of the sequence | 
**start** | **int** | The start value of the sequence | 
**value** | **int** | The last used value of the sequence | [optional] 
**cycle** | **bool** | Indicates if the sequence would start from minimun value once it reaches maximum value. If set to false, a failure would return if the sequence reaches maximum value. | 
**pattern** | **str** | The pattern to be used to generate next values in the sequence. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.sequence_definition import SequenceDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of SequenceDefinition from a JSON string
sequence_definition_instance = SequenceDefinition.from_json(json)
# print the JSON string representation of the object
print SequenceDefinition.to_json()

# convert the object into a dict
sequence_definition_dict = sequence_definition_instance.to_dict()
# create an instance of SequenceDefinition from a dict
sequence_definition_form_dict = sequence_definition.from_dict(sequence_definition_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


