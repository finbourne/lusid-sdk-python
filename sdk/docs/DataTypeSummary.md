# DataTypeSummary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_value_range** | **str** | Indicates the range of data acceptable by a data type. The available values are: Open, Closed | 
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | The display name of the data type. | 
**description** | **str** | The description of the data type. | 
**value_type** | **str** | The expected type of the values. The available values are: String, Int, Decimal, DateTime, Boolean, Map, List, PropertyArray, Percentage, Code, Id, Uri, CurrencyAndAmount, TradePrice, Currency, MetricValue, ResourceId, ResultValue, CutLocalTime, DateOrCutLabel, UnindexedText | 
**acceptable_values** | **List[str]** | The acceptable set of values for this data type. Only applies to &#39;open&#39; value type range. | [optional] 
**unit_schema** | **str** | The schema of the data type&#39;s units. The available values are: NoUnits, Basic, Iso4217Currency | [optional] 
**acceptable_units** | [**List[IUnitDefinitionDto]**](IUnitDefinitionDto.md) | The definitions of the acceptable units. | [optional] 

## Example

```python
from lusid.models.data_type_summary import DataTypeSummary

# TODO update the JSON string below
json = "{}"
# create an instance of DataTypeSummary from a JSON string
data_type_summary_instance = DataTypeSummary.from_json(json)
# print the JSON string representation of the object
print DataTypeSummary.to_json()

# convert the object into a dict
data_type_summary_dict = data_type_summary_instance.to_dict()
# create an instance of DataTypeSummary from a dict
data_type_summary_form_dict = data_type_summary.from_dict(data_type_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


