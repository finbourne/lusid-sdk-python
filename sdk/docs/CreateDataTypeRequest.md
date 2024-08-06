# CreateDataTypeRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The scope that the data type will be created in. | 
**code** | **str** | The code of the data type. Together with the scope this uniquely defines the data type. | 
**type_value_range** | **str** | Indicates the range of data acceptable by a data type. The available values are: Open, Closed | 
**display_name** | **str** | The display name of the data type. | 
**description** | **str** | The description of the data type. | 
**value_type** | **str** | The expected type of the values. The available values are: String, Int, Decimal, DateTime, Boolean, Map, List, PropertyArray, Percentage, Code, Id, Uri, CurrencyAndAmount, TradePrice, Currency, MetricValue, ResourceId, ResultValue, CutLocalTime, DateOrCutLabel, UnindexedText | 
**acceptable_values** | **List[str]** | The acceptable set of values for this data type. Only applies to &#39;open&#39; value type range. | [optional] 
**unit_schema** | **str** | The schema of the data type&#39;s units. The available values are: NoUnits, Basic, Iso4217Currency | [optional] 
**acceptable_units** | [**List[CreateUnitDefinition]**](CreateUnitDefinition.md) | The definitions of the acceptable units. | [optional] 
**reference_data** | [**ReferenceData**](ReferenceData.md) |  | [optional] 

## Example

```python
from lusid.models.create_data_type_request import CreateDataTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDataTypeRequest from a JSON string
create_data_type_request_instance = CreateDataTypeRequest.from_json(json)
# print the JSON string representation of the object
print CreateDataTypeRequest.to_json()

# convert the object into a dict
create_data_type_request_dict = create_data_type_request_instance.to_dict()
# create an instance of CreateDataTypeRequest from a dict
create_data_type_request_form_dict = create_data_type_request.from_dict(create_data_type_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


