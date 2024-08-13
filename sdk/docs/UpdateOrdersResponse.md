# UpdateOrdersResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**values** | [**Dict[str, Order]**](Order.md) | The orders which have been successfully updated. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The orders that could not be updated, along with a reason for their failure. | [optional] 
**metadata** | **Dict[str, List[ResponseMetaData]]** | Meta data associated with the update event. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.update_orders_response import UpdateOrdersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOrdersResponse from a JSON string
update_orders_response_instance = UpdateOrdersResponse.from_json(json)
# print the JSON string representation of the object
print UpdateOrdersResponse.to_json()

# convert the object into a dict
update_orders_response_dict = update_orders_response_instance.to_dict()
# create an instance of UpdateOrdersResponse from a dict
update_orders_response_form_dict = update_orders_response.from_dict(update_orders_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


