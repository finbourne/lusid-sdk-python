# PostCloseActivity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** |  | 
**entity_unique_id** | **str** |  | 
**as_at** | **datetime** |  | 

## Example

```python
from lusid.models.post_close_activity import PostCloseActivity

# TODO update the JSON string below
json = "{}"
# create an instance of PostCloseActivity from a JSON string
post_close_activity_instance = PostCloseActivity.from_json(json)
# print the JSON string representation of the object
print PostCloseActivity.to_json()

# convert the object into a dict
post_close_activity_dict = post_close_activity_instance.to_dict()
# create an instance of PostCloseActivity from a dict
post_close_activity_form_dict = post_close_activity.from_dict(post_close_activity_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


