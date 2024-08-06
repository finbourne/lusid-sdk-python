# FeeRuleUpsertRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**transaction_property_key** | **str** |  | 
**transaction_type** | **str** |  | 
**country** | **str** |  | 
**counterparty** | **str** |  | 
**transaction_currency** | **str** |  | 
**settlement_currency** | **str** |  | 
**execution_broker** | **str** |  | 
**custodian** | **str** |  | 
**exchange** | **str** |  | 
**fee** | [**CalculationInfo**](CalculationInfo.md) |  | 
**min_fee** | [**CalculationInfo**](CalculationInfo.md) |  | [optional] 
**max_fee** | [**CalculationInfo**](CalculationInfo.md) |  | [optional] 
**additional_keys** | **Dict[str, str]** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from lusid.models.fee_rule_upsert_request import FeeRuleUpsertRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FeeRuleUpsertRequest from a JSON string
fee_rule_upsert_request_instance = FeeRuleUpsertRequest.from_json(json)
# print the JSON string representation of the object
print FeeRuleUpsertRequest.to_json()

# convert the object into a dict
fee_rule_upsert_request_dict = fee_rule_upsert_request_instance.to_dict()
# create an instance of FeeRuleUpsertRequest from a dict
fee_rule_upsert_request_form_dict = fee_rule_upsert_request.from_dict(fee_rule_upsert_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


