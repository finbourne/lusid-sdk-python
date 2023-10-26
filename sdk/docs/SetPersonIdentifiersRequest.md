# SetPersonIdentifiersRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifiers** | [**Dict[str, ModelProperty]**](ModelProperty.md) | Identifiers to set for a Person. Identifiers not included in the request will not be amended. | [optional] 

## Example

```python
from lusid.models.set_person_identifiers_request import SetPersonIdentifiersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetPersonIdentifiersRequest from a JSON string
set_person_identifiers_request_instance = SetPersonIdentifiersRequest.from_json(json)
# print the JSON string representation of the object
print SetPersonIdentifiersRequest.to_json()

# convert the object into a dict
set_person_identifiers_request_dict = set_person_identifiers_request_instance.to_dict()
# create an instance of SetPersonIdentifiersRequest from a dict
set_person_identifiers_request_form_dict = set_person_identifiers_request.from_dict(set_person_identifiers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


