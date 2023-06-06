# Warning


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **str** |  | 
**message** | **str** |  | 

## Example

```python
from lusid.models.warning import Warning

# TODO update the JSON string below
json = "{}"
# create an instance of Warning from a JSON string
warning_instance = Warning.from_json(json)
# print the JSON string representation of the object
print Warning.to_json()

# convert the object into a dict
warning_dict = warning_instance.to_dict()
# create an instance of Warning from a dict
warning_form_dict = warning.from_dict(warning_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


