# UpsertPersonAccessMetadataRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**List[AccessMetadataValue]**](AccessMetadataValue.md) | The access control metadata to assign to a Person that matches the identifier | [optional] 

## Example

```python
from lusid.models.upsert_person_access_metadata_request import UpsertPersonAccessMetadataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertPersonAccessMetadataRequest from a JSON string
upsert_person_access_metadata_request_instance = UpsertPersonAccessMetadataRequest.from_json(json)
# print the JSON string representation of the object
print UpsertPersonAccessMetadataRequest.to_json()

# convert the object into a dict
upsert_person_access_metadata_request_dict = upsert_person_access_metadata_request_instance.to_dict()
# create an instance of UpsertPersonAccessMetadataRequest from a dict
upsert_person_access_metadata_request_form_dict = upsert_person_access_metadata_request.from_dict(upsert_person_access_metadata_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


