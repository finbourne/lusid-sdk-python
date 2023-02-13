# DataTypeSummary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_value_range** | **str** | Indicates the range of data acceptable by a data type. The available values are: Open, Closed | 
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | The display name of the data type. | 
**description** | **str** | The description of the data type. | 
**value_type** | **str** | The expected type of the values. The available values are: String, Int, Decimal, DateTime, Boolean, Map, List, PropertyArray, Percentage, Code, Id, Uri, CurrencyAndAmount, TradePrice, Currency, MetricValue, ResourceId, ResultValue, CutLocalTime, DateOrCutLabel, UnindexedText | 
**acceptable_values** | **list[str]** | The acceptable set of values for this data type. Only applies to &#39;open&#39; value type range. | [optional] 
**unit_schema** | **str** | The schema of the data type&#39;s units. The available values are: NoUnits, Basic, Iso4217Currency | [optional] 
**acceptable_units** | [**list[IUnitDefinitionDto]**](IUnitDefinitionDto.md) | The definitions of the acceptable units. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


