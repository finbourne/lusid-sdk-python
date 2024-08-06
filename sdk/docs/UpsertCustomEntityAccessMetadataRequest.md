# UpsertCustomEntityAccessMetadataRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**List[AccessMetadataValue]**](AccessMetadataValue.md) | The access control metadata to assign to a CustomEntity that matches the identifier | [optional] 

## Example

```python
from lusid.models.upsert_custom_entity_access_metadata_request import UpsertCustomEntityAccessMetadataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertCustomEntityAccessMetadataRequest from a JSON string
upsert_custom_entity_access_metadata_request_instance = UpsertCustomEntityAccessMetadataRequest.from_json(json)
# print the JSON string representation of the object
print UpsertCustomEntityAccessMetadataRequest.to_json()

# convert the object into a dict
upsert_custom_entity_access_metadata_request_dict = upsert_custom_entity_access_metadata_request_instance.to_dict()
# create an instance of UpsertCustomEntityAccessMetadataRequest from a dict
upsert_custom_entity_access_metadata_request_form_dict = upsert_custom_entity_access_metadata_request.from_dict(upsert_custom_entity_access_metadata_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


