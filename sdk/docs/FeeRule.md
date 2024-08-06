# FeeRule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
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
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.fee_rule import FeeRule

# TODO update the JSON string below
json = "{}"
# create an instance of FeeRule from a JSON string
fee_rule_instance = FeeRule.from_json(json)
# print the JSON string representation of the object
print FeeRule.to_json()

# convert the object into a dict
fee_rule_dict = fee_rule_instance.to_dict()
# create an instance of FeeRule from a dict
fee_rule_form_dict = fee_rule.from_dict(fee_rule_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


