# DataMapKey


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | The version of the mappings. It is possible that a client will wish to update mappings over time. The version identifies the MAJOR.MINOR.PATCH version  of the mappings that the client assigns it. | [optional] 
**code** | **str** | A unique name to semantically identify the mapping set. | [optional] 

## Example

```python
from lusid.models.data_map_key import DataMapKey

# TODO update the JSON string below
json = "{}"
# create an instance of DataMapKey from a JSON string
data_map_key_instance = DataMapKey.from_json(json)
# print the JSON string representation of the object
print DataMapKey.to_json()

# convert the object into a dict
data_map_key_dict = data_map_key_instance.to_dict()
# create an instance of DataMapKey from a dict
data_map_key_form_dict = data_map_key.from_dict(data_map_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


