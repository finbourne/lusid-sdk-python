# FundRequest

The request used to create a Fund.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code given for the Fund. | 
**display_name** | **str** | The name of the Fund. | [optional] 
**description** | **str** | A description for the Fund. | [optional] 
**abor_id** | [**ResourceId**](ResourceId.md) |  | 
**share_class_instrument_scopes** | **List[str]** | The scopes in which the instruments lie, currently limited to one. | [optional] 
**share_class_instruments** | [**List[InstrumentResolutionDetail]**](InstrumentResolutionDetail.md) | Details the user-provided instrument identifiers and the instrument resolved from them. | [optional] 
**type** | **str** | The type of fund; &#39;Standalone&#39;, &#39;Master&#39; or &#39;Feeder&#39; | 
**inception_date** | **datetime** | Inception date of the Fund | 
**decimal_places** | **int** | Number of decimal places for reporting | [optional] 
**year_end_date** | [**DayMonth**](DayMonth.md) |  | 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties for the Fund. | [optional] 

## Example

```python
from lusid.models.fund_request import FundRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FundRequest from a JSON string
fund_request_instance = FundRequest.from_json(json)
# print the JSON string representation of the object
print FundRequest.to_json()

# convert the object into a dict
fund_request_dict = fund_request_instance.to_dict()
# create an instance of FundRequest from a dict
fund_request_form_dict = fund_request.from_dict(fund_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


