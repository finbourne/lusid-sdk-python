# LoanPeriod


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_date** | **datetime** |  | 
**notional** | **float** |  | 
**interest_amount** | **float** |  | 

## Example

```python
from lusid.models.loan_period import LoanPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of LoanPeriod from a JSON string
loan_period_instance = LoanPeriod.from_json(json)
# print the JSON string representation of the object
print LoanPeriod.to_json()

# convert the object into a dict
loan_period_dict = loan_period_instance.to_dict()
# create an instance of LoanPeriod from a dict
loan_period_form_dict = loan_period.from_dict(loan_period_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


