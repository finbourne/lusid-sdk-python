# PortfolioHolding

A list of holdings.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_scope** | **str** | The scope in which the holding&#39;s instrument is in. | [optional] 
**instrument_uid** | **str** | The unique Lusid Instrument Id (LUID) of the instrument that the holding is in. | 
**sub_holding_keys** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | The sub-holding properties which identify the holding. Each property will be from the &#39;Transaction&#39; domain. These are configured on a transaction portfolio. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The properties which have been requested to be decorated onto the holding. These will be from the &#39;Instrument&#39; or &#39;Holding&#39; domain. | [optional] 
**holding_type** | **str** | The code for the type of the holding e.g. P, B, C, R, F etc. | 
**units** | **float** | The total number of units of the holding. | 
**settled_units** | **float** | The total number of settled units of the holding. | 
**cost** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**cost_portfolio_ccy** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**transaction** | [**Transaction**](Transaction.md) |  | [optional] 
**currency** | **str** | The holding currency. | [optional] 
**holding_type_name** | **str** | The decoded type of the holding e.g. Position, Balance, CashCommitment, Receivable, ForwardFX etc. | [optional] 
**holding_id** | **int** | A single identifier for the holding within the portfolio. The holdingId is constructed from the LusidInstrumentId, sub-holding keys and currrency and is unique within the portfolio. | [optional] 

## Example

```python
from lusid.models.portfolio_holding import PortfolioHolding

# TODO update the JSON string below
json = "{}"
# create an instance of PortfolioHolding from a JSON string
portfolio_holding_instance = PortfolioHolding.from_json(json)
# print the JSON string representation of the object
print PortfolioHolding.to_json()

# convert the object into a dict
portfolio_holding_dict = portfolio_holding_instance.to_dict()
# create an instance of PortfolioHolding from a dict
portfolio_holding_form_dict = portfolio_holding.from_dict(portfolio_holding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


