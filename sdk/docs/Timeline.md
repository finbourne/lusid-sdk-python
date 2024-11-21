# Timeline


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**display_name** | **str** | The name of the Timeline. | [optional] 
**description** | **str** | A description for the Timeline. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The Timelines properties. These will be from the &#39;Timeline&#39; domain. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested asAt datetime. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.timeline import Timeline

# TODO update the JSON string below
json = "{}"
# create an instance of Timeline from a JSON string
timeline_instance = Timeline.from_json(json)
# print the JSON string representation of the object
print Timeline.to_json()

# convert the object into a dict
timeline_dict = timeline_instance.to_dict()
# create an instance of Timeline from a dict
timeline_form_dict = timeline.from_dict(timeline_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


