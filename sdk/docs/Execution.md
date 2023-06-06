# Execution

The record of a number of executions against a single Placement (directly analogous to  a partial or full fill against a street order).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**placement_id** | [**ResourceId**](ResourceId.md) |  | 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Client-defined properties associated with this execution. | [optional] 
**instrument_identifiers** | **Dict[str, str]** | The instrument ordered. | 
**lusid_instrument_id** | **str** | The LUSID instrument id for the instrument execution. | 
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
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.execution import Execution

# TODO update the JSON string below
json = "{}"
# create an instance of Execution from a JSON string
execution_instance = Execution.from_json(json)
# print the JSON string representation of the object
print Execution.to_json()

# convert the object into a dict
execution_dict = execution_instance.to_dict()
# create an instance of Execution from a dict
execution_form_dict = execution.from_dict(execution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


