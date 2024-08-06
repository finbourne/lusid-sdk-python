# AccessMetadataValue

An access control value. Provider should only be used if you are a service provide licensing data. In that case  the provider value must match your domain.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | 
**provider** | **str** |  | [optional] 

## Example

```python
from lusid.models.access_metadata_value import AccessMetadataValue

# TODO update the JSON string below
json = "{}"
# create an instance of AccessMetadataValue from a JSON string
access_metadata_value_instance = AccessMetadataValue.from_json(json)
# print the JSON string representation of the object
print AccessMetadataValue.to_json()

# convert the object into a dict
access_metadata_value_dict = access_metadata_value_instance.to_dict()
# create an instance of AccessMetadataValue from a dict
access_metadata_value_form_dict = access_metadata_value.from_dict(access_metadata_value_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


