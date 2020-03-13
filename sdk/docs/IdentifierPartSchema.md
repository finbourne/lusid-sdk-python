# IdentifierPartSchema

The schema of an contributing part of a valid LUSID resource identifier
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | The typical index in the identifier in which this part appears | [readonly] 
**name** | **str** | The name of the identifier part that can/should be provided for this resource type | [readonly] 
**display_name** | **str** | The display name of the identifier part | [readonly] 
**description** | **str** | A brief description of the point of this identifier part | [readonly] 
**required** | **bool** | Whether a value is required to be provided | [readonly] 
**links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


