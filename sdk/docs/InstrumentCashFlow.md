# InstrumentCashFlow

The details for the cashflow associated with an instrument from a given portfolio.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_date** | **datetime** | The date at which the given cash flow is due to be paid (SettlementDate is used somewhat interchangeably with PaymentDate.) | 
**amount** | **float** | The quantity (amount) that will be paid. Note that this can be empty if the payment is in the future and a model is used that cannot estimate it. | [optional] 
**currency** | **str** | The payment currency of the cash flow. | 
**source_portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**source_transaction_id** | **str** | The identifier for the parent transaction on the instrument that will pay/receive this cash flow. | 
**source_instrument_scope** | **str** | The unqiue Lusid Instrument Id (LUID) of the instrument that the holding is in. | 
**source_instrument_id** | **str** | The unqiue Lusid Instrument Id (LUID) of the instrument that the holding is in. | 
**diagnostics** | **Dict[str, str]** | Whilst a cash flow is defined by an (amount,ccy) pair and the date it is paid on there is additional information required for diagnostics. This includes a range of information and can be empty in the case of a simple cash quantity or where further information is not available. Typical information includes items such as reset dates, RIC, accrual start/end, number of days and curve data. | 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.instrument_cash_flow import InstrumentCashFlow

# TODO update the JSON string below
json = "{}"
# create an instance of InstrumentCashFlow from a JSON string
instrument_cash_flow_instance = InstrumentCashFlow.from_json(json)
# print the JSON string representation of the object
print InstrumentCashFlow.to_json()

# convert the object into a dict
instrument_cash_flow_dict = instrument_cash_flow_instance.to_dict()
# create an instance of InstrumentCashFlow from a dict
instrument_cash_flow_form_dict = instrument_cash_flow.from_dict(instrument_cash_flow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


