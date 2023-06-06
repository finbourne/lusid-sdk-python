# ExecutionRequest

A request to create or update a Execution.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**placement_id** | [**ResourceId**](ResourceId.md) |  | 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Client-defined properties associated with this execution. | [optional] 
**instrument_identifiers** | **Dict[str, str]** | The instrument ordered. | 
**quantity** | **float** | The quantity of given instrument ordered. | 
**state** | **str** | The state of this execution (typically a FIX state; Open, Filled, etc). | 
**side** | **str** | The side (Buy, Sell, ...) of this execution. | 
**type** | **str** | The type of this execution (Market, Limit, etc). | 
**created_date** | **datetime** | The active date of this execution. | 
**settlement_date** | **datetime** | The (optional) settlement date for this execution | [optional] 
**price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**settlement_currency** | **str** | The execution&#39;s settlement currency. | 
**settlement_currency_fx_rate** | **float** | The exectuion&#39;s settlement currency rate. | 
**counterparty** | **str** | The market entity this placement is placed with. | 
**average_price** | **float** | The average price of all executions for a given placement at the time of upsert | [optional] 

## Example

```python
from lusid.models.execution_request import ExecutionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionRequest from a JSON string
execution_request_instance = ExecutionRequest.from_json(json)
# print the JSON string representation of the object
print ExecutionRequest.to_json()

# convert the object into a dict
execution_request_dict = execution_request_instance.to_dict()
# create an instance of ExecutionRequest from a dict
execution_request_form_dict = execution_request.from_dict(execution_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


