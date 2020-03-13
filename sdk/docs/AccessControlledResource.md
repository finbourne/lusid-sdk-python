# AccessControlledResource

A resource to which access can be controlled
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application** | **str** | The application to which this resource belongs | [optional] 
**name** | **str** | The display name of the resource | [optional] 
**description** | **str** | The description of the resource | 
**actions** | [**list[AccessControlledAction]**](AccessControlledAction.md) | The actions acceptable for this type of resource | 
**identifier_parts** | [**list[IdentifierPartSchema]**](IdentifierPartSchema.md) | The constituent parts of a valid identifier for this resource | [optional] 
**links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


