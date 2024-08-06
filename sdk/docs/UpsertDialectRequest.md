# UpsertDialectRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**DialectId**](DialectId.md) |  | 
**var_schema** | [**DialectSchema**](DialectSchema.md) |  | 

## Example

```python
from lusid.models.upsert_dialect_request import UpsertDialectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertDialectRequest from a JSON string
upsert_dialect_request_instance = UpsertDialectRequest.from_json(json)
# print the JSON string representation of the object
print UpsertDialectRequest.to_json()

# convert the object into a dict
upsert_dialect_request_dict = upsert_dialect_request_instance.to_dict()
# create an instance of UpsertDialectRequest from a dict
upsert_dialect_request_form_dict = upsert_dialect_request.from_dict(upsert_dialect_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


