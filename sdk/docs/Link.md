# Link


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relation** | **str** |  | 
**href** | **str** |  | 
**description** | **str** |  | [optional] 
**method** | **str** |  | 

## Example

```python
from lusid.models.link import Link

# TODO update the JSON string below
json = "{}"
# create an instance of Link from a JSON string
link_instance = Link.from_json(json)
# print the JSON string representation of the object
print Link.to_json()

# convert the object into a dict
link_dict = link_instance.to_dict()
# create an instance of Link from a dict
link_form_dict = link.from_dict(link_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


