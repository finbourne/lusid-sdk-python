# UpsertLegalEntityAccessMetadataRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**List[AccessMetadataValue]**](AccessMetadataValue.md) | The access control metadata to assign to a Legal Entity that matches the identifier | [optional] 

## Example

```python
from lusid.models.upsert_legal_entity_access_metadata_request import UpsertLegalEntityAccessMetadataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertLegalEntityAccessMetadataRequest from a JSON string
upsert_legal_entity_access_metadata_request_instance = UpsertLegalEntityAccessMetadataRequest.from_json(json)
# print the JSON string representation of the object
print UpsertLegalEntityAccessMetadataRequest.to_json()

# convert the object into a dict
upsert_legal_entity_access_metadata_request_dict = upsert_legal_entity_access_metadata_request_instance.to_dict()
# create an instance of UpsertLegalEntityAccessMetadataRequest from a dict
upsert_legal_entity_access_metadata_request_form_dict = upsert_legal_entity_access_metadata_request.from_dict(upsert_legal_entity_access_metadata_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


