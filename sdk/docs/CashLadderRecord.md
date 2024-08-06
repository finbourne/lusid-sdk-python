# CashLadderRecord


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_date** | **datetime** |  | [optional] 
**open** | **float** |  | 
**activities** | **Dict[str, float]** |  | 
**close** | **float** |  | 

## Example

```python
from lusid.models.cash_ladder_record import CashLadderRecord

# TODO update the JSON string below
json = "{}"
# create an instance of CashLadderRecord from a JSON string
cash_ladder_record_instance = CashLadderRecord.from_json(json)
# print the JSON string representation of the object
print CashLadderRecord.to_json()

# convert the object into a dict
cash_ladder_record_dict = cash_ladder_record_instance.to_dict()
# create an instance of CashLadderRecord from a dict
cash_ladder_record_form_dict = cash_ladder_record.from_dict(cash_ladder_record_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


