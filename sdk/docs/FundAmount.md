# FundAmount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** | The value of the amount. | [optional] 

## Example

```python
from lusid.models.fund_amount import FundAmount

# TODO update the JSON string below
json = "{}"
# create an instance of FundAmount from a JSON string
fund_amount_instance = FundAmount.from_json(json)
# print the JSON string representation of the object
print FundAmount.to_json()

# convert the object into a dict
fund_amount_dict = fund_amount_instance.to_dict()
# create an instance of FundAmount from a dict
fund_amount_form_dict = fund_amount.from_dict(fund_amount_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


