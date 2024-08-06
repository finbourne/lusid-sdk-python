# ComponentFilter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_id** | **str** |  | 
**filter** | **str** |  | 

## Example

```python
from lusid.models.component_filter import ComponentFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ComponentFilter from a JSON string
component_filter_instance = ComponentFilter.from_json(json)
# print the JSON string representation of the object
print ComponentFilter.to_json()

# convert the object into a dict
component_filter_dict = component_filter_instance.to_dict()
# create an instance of ComponentFilter from a dict
component_filter_form_dict = component_filter.from_dict(component_filter_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


