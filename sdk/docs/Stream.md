# Stream


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_read** | **bool** |  | [optional] [readonly] 
**can_write** | **bool** |  | [optional] [readonly] 
**can_seek** | **bool** |  | [optional] [readonly] 
**can_timeout** | **bool** |  | [optional] [readonly] 
**length** | **int** |  | [optional] [readonly] 
**position** | **int** |  | [optional] 
**read_timeout** | **int** |  | [optional] 
**write_timeout** | **int** |  | [optional] 

## Example

```python
from lusid.models.stream import Stream

# TODO update the JSON string below
json = "{}"
# create an instance of Stream from a JSON string
stream_instance = Stream.from_json(json)
# print the JSON string representation of the object
print Stream.to_json()

# convert the object into a dict
stream_dict = stream_instance.to_dict()
# create an instance of Stream from a dict
stream_form_dict = stream.from_dict(stream_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


