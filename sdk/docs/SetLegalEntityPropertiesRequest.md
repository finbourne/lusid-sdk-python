# SetLegalEntityPropertiesRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | Properties to set for a Legal Entity. All time-variant properties must have same EffectiveFrom date. Properties not included in the request will not be amended. | [optional] 

## Example

```python
from lusid.models.set_legal_entity_properties_request import SetLegalEntityPropertiesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetLegalEntityPropertiesRequest from a JSON string
set_legal_entity_properties_request_instance = SetLegalEntityPropertiesRequest.from_json(json)
# print the JSON string representation of the object
print SetLegalEntityPropertiesRequest.to_json()

# convert the object into a dict
set_legal_entity_properties_request_dict = set_legal_entity_properties_request_instance.to_dict()
# create an instance of SetLegalEntityPropertiesRequest from a dict
set_legal_entity_properties_request_form_dict = set_legal_entity_properties_request.from_dict(set_legal_entity_properties_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


