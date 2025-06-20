# PostCloseActivitiesRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**post_close_activities** | [**List[PostCloseActivity]**](PostCloseActivity.md) | Collection of post close activites. | 

## Example

```python
from lusid.models.post_close_activities_request import PostCloseActivitiesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostCloseActivitiesRequest from a JSON string
post_close_activities_request_instance = PostCloseActivitiesRequest.from_json(json)
# print the JSON string representation of the object
print PostCloseActivitiesRequest.to_json()

# convert the object into a dict
post_close_activities_request_dict = post_close_activities_request_instance.to_dict()
# create an instance of PostCloseActivitiesRequest from a dict
post_close_activities_request_form_dict = post_close_activities_request.from_dict(post_close_activities_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


