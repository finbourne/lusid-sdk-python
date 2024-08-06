# Participation

The record an order's participation in a specific placement.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**placement_id** | [**ResourceId**](ResourceId.md) |  | 
**order_id** | [**ResourceId**](ResourceId.md) |  | 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.participation import Participation

# TODO update the JSON string below
json = "{}"
# create an instance of Participation from a JSON string
participation_instance = Participation.from_json(json)
# print the JSON string representation of the object
print Participation.to_json()

# convert the object into a dict
participation_dict = participation_instance.to_dict()
# create an instance of Participation from a dict
participation_form_dict = participation.from_dict(participation_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


