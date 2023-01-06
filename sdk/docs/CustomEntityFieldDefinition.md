# CustomEntityFieldDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the field. | 
**lifetime** | **str** | Describes how the field’s values can change over time. The available values are: “Perpetual”, “TimeVariant”. | 
**type** | **str** | The value type for the field. Available values are: “String”, “Boolean”, “DateTime”, “Decimal”. | 
**collection_type** | **str** | The collection type for the field. Available values are: “Single”, “Array”. Null value defaults to “Single” | [optional] 
**required** | **bool** | Whether the field is required or not. | 
**description** | **str** | An optional description for the field. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


