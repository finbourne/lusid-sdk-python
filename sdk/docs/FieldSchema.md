# FieldSchema


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**display_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**type** | **str** | The available values are: String, Int, Decimal, DateTime, Boolean, Map, List, PropertyArray, Percentage, Code, Id, Uri, CurrencyAndAmount, TradePrice, Currency, MetricValue, ResourceId, ResultValue, CutLocalTime, DateOrCutLabel, UnindexedText | [optional] 
**display_order** | **int** |  | [optional] 

## Example

```python
from lusid.models.field_schema import FieldSchema

# TODO update the JSON string below
json = "{}"
# create an instance of FieldSchema from a JSON string
field_schema_instance = FieldSchema.from_json(json)
# print the JSON string representation of the object
print FieldSchema.to_json()

# convert the object into a dict
field_schema_dict = field_schema_instance.to_dict()
# create an instance of FieldSchema from a dict
field_schema_form_dict = field_schema.from_dict(field_schema_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


