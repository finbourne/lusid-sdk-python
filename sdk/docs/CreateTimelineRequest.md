# CreateTimelineRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | The name of the Timeline. | 
**description** | **str** | A description for the Timeline. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The Timelines properties. These will be from the &#39;Timeline&#39; domain. | [optional] 

## Example

```python
from lusid.models.create_timeline_request import CreateTimelineRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTimelineRequest from a JSON string
create_timeline_request_instance = CreateTimelineRequest.from_json(json)
# print the JSON string representation of the object
print CreateTimelineRequest.to_json()

# convert the object into a dict
create_timeline_request_dict = create_timeline_request_instance.to_dict()
# create an instance of CreateTimelineRequest from a dict
create_timeline_request_form_dict = create_timeline_request.from_dict(create_timeline_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


