# MetadataKeyValueResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **Dict[str, List[AccessMetadataValue]]** |  | 

## Example

```python
from lusid.models.metadata_key_value_response import MetadataKeyValueResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataKeyValueResponse from a JSON string
metadata_key_value_response_instance = MetadataKeyValueResponse.from_json(json)
# print the JSON string representation of the object
print MetadataKeyValueResponse.to_json()

# convert the object into a dict
metadata_key_value_response_dict = metadata_key_value_response_instance.to_dict()
# create an instance of MetadataKeyValueResponse from a dict
metadata_key_value_response_form_dict = metadata_key_value_response.from_dict(metadata_key_value_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


