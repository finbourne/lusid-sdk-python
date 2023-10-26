# SetPersonPropertiesRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | Properties to set for a Person. All time-variant properties must have same EffectiveFrom date. Properties not included in the request will not be amended. | 

## Example

```python
from lusid.models.set_person_properties_request import SetPersonPropertiesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetPersonPropertiesRequest from a JSON string
set_person_properties_request_instance = SetPersonPropertiesRequest.from_json(json)
# print the JSON string representation of the object
print SetPersonPropertiesRequest.to_json()

# convert the object into a dict
set_person_properties_request_dict = set_person_properties_request_instance.to_dict()
# create an instance of SetPersonPropertiesRequest from a dict
set_person_properties_request_form_dict = set_person_properties_request.from_dict(set_person_properties_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


