# UpdateFeeTypeRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the fee type. | 
**description** | **str** | The description of the fee type. | [optional] 
**component_transactions** | [**List[ComponentTransaction]**](ComponentTransaction.md) | A set of component transactions that relate to the fee type to be updated. | 

## Example

```python
from lusid.models.update_fee_type_request import UpdateFeeTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFeeTypeRequest from a JSON string
update_fee_type_request_instance = UpdateFeeTypeRequest.from_json(json)
# print the JSON string representation of the object
print UpdateFeeTypeRequest.to_json()

# convert the object into a dict
update_fee_type_request_dict = update_fee_type_request_instance.to_dict()
# create an instance of UpdateFeeTypeRequest from a dict
update_fee_type_request_form_dict = update_fee_type_request.from_dict(update_fee_type_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


