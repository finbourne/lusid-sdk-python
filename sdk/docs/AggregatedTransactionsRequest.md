# AggregatedTransactionsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_transaction_date** | **datetime** |  | 
**to_transaction_date** | **datetime** |  | 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**as_at** | **datetime** |  | [optional] 
**metrics** | [**List[AggregateSpec]**](AggregateSpec.md) |  | 
**group_by** | **List[str]** |  | [optional] 
**filters** | [**List[PropertyFilter]**](PropertyFilter.md) |  | [optional] 
**sort** | [**List[OrderBySpec]**](OrderBySpec.md) |  | [optional] 

## Example

```python
from lusid.models.aggregated_transactions_request import AggregatedTransactionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AggregatedTransactionsRequest from a JSON string
aggregated_transactions_request_instance = AggregatedTransactionsRequest.from_json(json)
# print the JSON string representation of the object
print AggregatedTransactionsRequest.to_json()

# convert the object into a dict
aggregated_transactions_request_dict = aggregated_transactions_request_instance.to_dict()
# create an instance of AggregatedTransactionsRequest from a dict
aggregated_transactions_request_form_dict = aggregated_transactions_request.from_dict(aggregated_transactions_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


