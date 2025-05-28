# CalculateOrderDatesResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successes** | [**Dict[str, TransferAgencyDates]**](TransferAgencyDates.md) | A dictionary of successful date calculations, keyed by the request key. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | A dictionary of failed date calculations, keyed by the request key, containing the error details of any failures that occurred during the calculation. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.calculate_order_dates_response import CalculateOrderDatesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CalculateOrderDatesResponse from a JSON string
calculate_order_dates_response_instance = CalculateOrderDatesResponse.from_json(json)
# print the JSON string representation of the object
print CalculateOrderDatesResponse.to_json()

# convert the object into a dict
calculate_order_dates_response_dict = calculate_order_dates_response_instance.to_dict()
# create an instance of CalculateOrderDatesResponse from a dict
calculate_order_dates_response_form_dict = calculate_order_dates_response.from_dict(calculate_order_dates_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


