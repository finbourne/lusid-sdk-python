# UpdateTimelineRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the Timeline. | 
**description** | **str** | A description for the Timeline. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The Timelines properties. These will be from the &#39;Timeline&#39; domain. | [optional] 

## Example

```python
from lusid.models.update_timeline_request import UpdateTimelineRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTimelineRequest from a JSON string
update_timeline_request_instance = UpdateTimelineRequest.from_json(json)
# print the JSON string representation of the object
print UpdateTimelineRequest.to_json()

# convert the object into a dict
update_timeline_request_dict = update_timeline_request_instance.to_dict()
# create an instance of UpdateTimelineRequest from a dict
update_timeline_request_form_dict = update_timeline_request.from_dict(update_timeline_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


