# ParticipationSetRequest

A request to create or update multiple Participations.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**List[ParticipationRequest]**](ParticipationRequest.md) | A collection of ParticipationRequests. | [optional] 

## Example

```python
from lusid.models.participation_set_request import ParticipationSetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ParticipationSetRequest from a JSON string
participation_set_request_instance = ParticipationSetRequest.from_json(json)
# print the JSON string representation of the object
print ParticipationSetRequest.to_json()

# convert the object into a dict
participation_set_request_dict = participation_set_request_instance.to_dict()
# create an instance of ParticipationSetRequest from a dict
participation_set_request_form_dict = participation_set_request.from_dict(participation_set_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


