# SetLegalEntityIdentifiersRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifiers** | [**Dict[str, ModelProperty]**](ModelProperty.md) | Identifiers to set for a Legal Entity. Identifiers not included in the request will not be amended. | [optional] 

## Example

```python
from lusid.models.set_legal_entity_identifiers_request import SetLegalEntityIdentifiersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetLegalEntityIdentifiersRequest from a JSON string
set_legal_entity_identifiers_request_instance = SetLegalEntityIdentifiersRequest.from_json(json)
# print the JSON string representation of the object
print SetLegalEntityIdentifiersRequest.to_json()

# convert the object into a dict
set_legal_entity_identifiers_request_dict = set_legal_entity_identifiers_request_instance.to_dict()
# create an instance of SetLegalEntityIdentifiersRequest from a dict
set_legal_entity_identifiers_request_form_dict = set_legal_entity_identifiers_request.from_dict(set_legal_entity_identifiers_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


