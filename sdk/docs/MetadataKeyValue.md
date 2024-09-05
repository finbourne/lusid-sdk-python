# MetadataKeyValue


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **Dict[str, List[AccessMetadataValue]]** |  | 

## Example

```python
from lusid.models.metadata_key_value import MetadataKeyValue

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataKeyValue from a JSON string
metadata_key_value_instance = MetadataKeyValue.from_json(json)
# print the JSON string representation of the object
print MetadataKeyValue.to_json()

# convert the object into a dict
metadata_key_value_dict = metadata_key_value_instance.to_dict()
# create an instance of MetadataKeyValue from a dict
metadata_key_value_form_dict = metadata_key_value.from_dict(metadata_key_value_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


