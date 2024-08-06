# CreateSequenceRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code of the sequence definition to create | 
**increment** | **int** | The value to increment between each value in the sequence | [optional] 
**min_value** | **int** | The minimum value of the sequence | [optional] 
**max_value** | **int** | The maximum value of the sequence | [optional] 
**start** | **int** | The start value of the sequence | [optional] 
**cycle** | **bool** | Set to true to start the sequence over again when it reaches the end. Defaults to false if not provided. | [optional] 
**pattern** | **str** | The pattern to be used to generate next values in the sequence. Defaults to null if not provided. | [optional] 

## Example

```python
from lusid.models.create_sequence_request import CreateSequenceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSequenceRequest from a JSON string
create_sequence_request_instance = CreateSequenceRequest.from_json(json)
# print the JSON string representation of the object
print CreateSequenceRequest.to_json()

# convert the object into a dict
create_sequence_request_dict = create_sequence_request_instance.to_dict()
# create an instance of CreateSequenceRequest from a dict
create_sequence_request_form_dict = create_sequence_request.from_dict(create_sequence_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


