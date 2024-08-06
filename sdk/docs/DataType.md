# DataType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**type_value_range** | **str** | The available values are: Open, Closed | 
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** |  | 
**description** | **str** |  | 
**value_type** | **str** | The available values are: String, Int, Decimal, DateTime, Boolean, Map, List, PropertyArray, Percentage, Code, Id, Uri, CurrencyAndAmount, TradePrice, Currency, MetricValue, ResourceId, ResultValue, CutLocalTime, DateOrCutLabel, UnindexedText | 
**acceptable_values** | **List[str]** |  | [optional] 
**unit_schema** | **str** | The available values are: NoUnits, Basic, Iso4217Currency | [optional] 
**acceptable_units** | [**List[IUnitDefinitionDto]**](IUnitDefinitionDto.md) |  | [optional] 
**reference_data** | [**ReferenceData**](ReferenceData.md) |  | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.data_type import DataType

# TODO update the JSON string below
json = "{}"
# create an instance of DataType from a JSON string
data_type_instance = DataType.from_json(json)
# print the JSON string representation of the object
print DataType.to_json()

# convert the object into a dict
data_type_dict = data_type_instance.to_dict()
# create an instance of DataType from a dict
data_type_form_dict = data_type.from_dict(data_type_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


