# CalculateOrderDatesRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_identifier_type** | **str** |  | 
**instrument_identifier** | **str** |  | 
**instrument_scope** | **str** |  | [optional] 
**received_date** | **datetime** |  | [optional] 
**price_date** | **datetime** |  | [optional] 
**transaction_category** | **str** |  | [optional] 
**liquidating_share_class_identifier** | **str** |  | [optional] 
**liquidating_share_class_identifier_type** | **str** |  | [optional] 
**liquidating_share_class_instrument_scope** | **str** |  | [optional] 

## Example

```python
from lusid.models.calculate_order_dates_request import CalculateOrderDatesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CalculateOrderDatesRequest from a JSON string
calculate_order_dates_request_instance = CalculateOrderDatesRequest.from_json(json)
# print the JSON string representation of the object
print CalculateOrderDatesRequest.to_json()

# convert the object into a dict
calculate_order_dates_request_dict = calculate_order_dates_request_instance.to_dict()
# create an instance of CalculateOrderDatesRequest from a dict
calculate_order_dates_request_form_dict = calculate_order_dates_request.from_dict(calculate_order_dates_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


