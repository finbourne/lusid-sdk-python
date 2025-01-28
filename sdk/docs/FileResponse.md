# FileResponse

Allows a file (represented as a stream) to be returned from an Api call

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_stream** | **bytearray** |  | [optional] 
**content_type** | **str** |  | [optional] 
**downloaded_filename** | **str** |  | [optional] 

## Example

```python
from lusid.models.file_response import FileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FileResponse from a JSON string
file_response_instance = FileResponse.from_json(json)
# print the JSON string representation of the object
print FileResponse.to_json()

# convert the object into a dict
file_response_dict = file_response_instance.to_dict()
# create an instance of FileResponse from a dict
file_response_form_dict = file_response.from_dict(file_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


