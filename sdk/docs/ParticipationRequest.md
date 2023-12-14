# ParticipationRequest

A request to create or update a Participation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**placement_id** | [**ResourceId**](ResourceId.md) |  | 
**order_id** | [**ResourceId**](ResourceId.md) |  | 

## Example

```python
from lusid.models.participation_request import ParticipationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ParticipationRequest from a JSON string
participation_request_instance = ParticipationRequest.from_json(json)
# print the JSON string representation of the object
print ParticipationRequest.to_json()

# convert the object into a dict
participation_request_dict = participation_request_instance.to_dict()
# create an instance of ParticipationRequest from a dict
participation_request_form_dict = participation_request.from_dict(participation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


