# FeeTypeRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**name** | **str** | The name of the fee type. | 
**description** | **str** | The description of the fee type. | [optional] 
**component_transactions** | [**List[ComponentTransaction]**](ComponentTransaction.md) | A set of component transactions that relate to the fee type to be created. | 

## Example

```python
from lusid.models.fee_type_request import FeeTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FeeTypeRequest from a JSON string
fee_type_request_instance = FeeTypeRequest.from_json(json)
# print the JSON string representation of the object
print FeeTypeRequest.to_json()

# convert the object into a dict
fee_type_request_dict = fee_type_request_instance.to_dict()
# create an instance of FeeTypeRequest from a dict
fee_type_request_form_dict = fee_type_request.from_dict(fee_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


