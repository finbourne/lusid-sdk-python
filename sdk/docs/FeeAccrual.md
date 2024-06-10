# FeeAccrual


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_at** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**calculation_base** | **float** |  | [optional] 
**amount** | **float** |  | [optional] 
**previous_accrual** | **float** |  | [optional] 
**total_accrual** | **float** |  | [optional] [readonly] 

## Example

```python
from lusid.models.fee_accrual import FeeAccrual

# TODO update the JSON string below
json = "{}"
# create an instance of FeeAccrual from a JSON string
fee_accrual_instance = FeeAccrual.from_json(json)
# print the JSON string representation of the object
print FeeAccrual.to_json()

# convert the object into a dict
fee_accrual_dict = fee_accrual_instance.to_dict()
# create an instance of FeeAccrual from a dict
fee_accrual_form_dict = fee_accrual.from_dict(fee_accrual_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


