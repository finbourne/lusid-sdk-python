# MappingRule

An individual mapping rule, for mapping between a left and right field/property.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | **str** | The name of the field/property in the left resource (e.g. a transaction) | [optional] 
**right** | **str** | The name of the field/property in the right resource (e.g. a transaction) | [optional] 
**comparison_type** | **str** | The type of comparison to be performed | [optional] 
**comparison_value** | **float** | The (optional) value used with Finbourne.WebApi.Interface.Dto.Mappings.MappingRule.ComparisonType | [optional] 
**weight** | **float** | A factor used to influence the importance of this item. | [optional] 
**mapped_strings** | [**list[MappedString]**](MappedString.md) | The (optional) value used to map string values. | [optional] 
**is_case_sensitive** | **bool** | Should string comparisons take case into account, defaults to &#x60;false&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


