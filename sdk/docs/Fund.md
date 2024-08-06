# Fund

A Fund entity.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | The name of the Fund. | [optional] 
**description** | **str** | A description for the Fund. | [optional] 
**fund_configuration_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**abor_id** | [**ResourceId**](ResourceId.md) |  | 
**share_class_instruments** | [**List[InstrumentResolutionDetail]**](InstrumentResolutionDetail.md) | Details the user-provided instrument identifiers and the instrument resolved from them. | [optional] 
**type** | **str** | The type of fund; &#39;Standalone&#39;, &#39;Master&#39; or &#39;Feeder&#39; | 
**inception_date** | **datetime** | Inception date of the Fund | 
**decimal_places** | **int** | Number of decimal places for reporting | [optional] 
**year_end_date** | [**DayMonth**](DayMonth.md) |  | 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties for the Fund. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.fund import Fund

# TODO update the JSON string below
json = "{}"
# create an instance of Fund from a JSON string
fund_instance = Fund.from_json(json)
# print the JSON string representation of the object
print Fund.to_json()

# convert the object into a dict
fund_dict = fund_instance.to_dict()
# create an instance of Fund from a dict
fund_form_dict = fund.from_dict(fund_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


