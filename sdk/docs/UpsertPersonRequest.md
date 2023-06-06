# UpsertPersonRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifiers** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The identifiers the person will be upserted with.The provided keys should be idTypeScope, idTypeCode, code | 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties associated to the Person. There can be multiple properties associated with a property key. | [optional] 
**display_name** | **str** | The display name of the Person | 
**description** | **str** | The description of the Person | [optional] 

## Example

```python
from lusid.models.upsert_person_request import UpsertPersonRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertPersonRequest from a JSON string
upsert_person_request_instance = UpsertPersonRequest.from_json(json)
# print the JSON string representation of the object
print UpsertPersonRequest.to_json()

# convert the object into a dict
upsert_person_request_dict = upsert_person_request_instance.to_dict()
# create an instance of UpsertPersonRequest from a dict
upsert_person_request_form_dict = upsert_person_request.from_dict(upsert_person_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


