# FeeRuleUpsertResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**Dict[str, FeeRule]**](FeeRule.md) |  | 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.fee_rule_upsert_response import FeeRuleUpsertResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FeeRuleUpsertResponse from a JSON string
fee_rule_upsert_response_instance = FeeRuleUpsertResponse.from_json(json)
# print the JSON string representation of the object
print FeeRuleUpsertResponse.to_json()

# convert the object into a dict
fee_rule_upsert_response_dict = fee_rule_upsert_response_instance.to_dict()
# create an instance of FeeRuleUpsertResponse from a dict
fee_rule_upsert_response_form_dict = fee_rule_upsert_response.from_dict(fee_rule_upsert_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


