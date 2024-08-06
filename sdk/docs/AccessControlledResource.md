# AccessControlledResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | 
**actions** | [**List[AccessControlledAction]**](AccessControlledAction.md) |  | 
**identifier_parts** | [**List[IdentifierPartSchema]**](IdentifierPartSchema.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.access_controlled_resource import AccessControlledResource

# TODO update the JSON string below
json = "{}"
# create an instance of AccessControlledResource from a JSON string
access_controlled_resource_instance = AccessControlledResource.from_json(json)
# print the JSON string representation of the object
print AccessControlledResource.to_json()

# convert the object into a dict
access_controlled_resource_dict = access_controlled_resource_instance.to_dict()
# create an instance of AccessControlledResource from a dict
access_controlled_resource_form_dict = access_controlled_resource.from_dict(access_controlled_resource_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


