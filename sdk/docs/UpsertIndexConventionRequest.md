# UpsertIndexConventionRequest

Index convention that is to be stored in the convention data store.  Only one of these must be present.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index_convention** | [**IndexConvention**](IndexConvention.md) |  | [optional] 

## Example

```python
from lusid.models.upsert_index_convention_request import UpsertIndexConventionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertIndexConventionRequest from a JSON string
upsert_index_convention_request_instance = UpsertIndexConventionRequest.from_json(json)
# print the JSON string representation of the object
print UpsertIndexConventionRequest.to_json()

# convert the object into a dict
upsert_index_convention_request_dict = upsert_index_convention_request_instance.to_dict()
# create an instance of UpsertIndexConventionRequest from a dict
upsert_index_convention_request_form_dict = upsert_index_convention_request.from_dict(upsert_index_convention_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


