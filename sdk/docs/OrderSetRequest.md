# OrderSetRequest

A request to create or update multiple Orders.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_requests** | [**List[OrderRequest]**](OrderRequest.md) | A collection of OrderRequests. | [optional] 

## Example

```python
from lusid.models.order_set_request import OrderSetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrderSetRequest from a JSON string
order_set_request_instance = OrderSetRequest.from_json(json)
# print the JSON string representation of the object
print OrderSetRequest.to_json()

# convert the object into a dict
order_set_request_dict = order_set_request_instance.to_dict()
# create an instance of OrderSetRequest from a dict
order_set_request_form_dict = order_set_request.from_dict(order_set_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


