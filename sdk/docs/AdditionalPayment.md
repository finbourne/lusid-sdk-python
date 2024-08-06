# AdditionalPayment

Record describing additional payment entity.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The upfront amount. | 
**currency** | **str** | The upfront currency. | 
**pay_date** | **datetime** | Date when the upfront is paid. | 
**pay_receive** | **str** | Is it pay or receive.    Supported string (enumeration) values are: [Pay, Receive]. | 

## Example

```python
from lusid.models.additional_payment import AdditionalPayment

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalPayment from a JSON string
additional_payment_instance = AdditionalPayment.from_json(json)
# print the JSON string representation of the object
print AdditionalPayment.to_json()

# convert the object into a dict
additional_payment_dict = additional_payment_instance.to_dict()
# create an instance of AdditionalPayment from a dict
additional_payment_form_dict = additional_payment.from_dict(additional_payment_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


