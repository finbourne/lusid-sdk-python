# RealisedGainLoss


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_scope** | **str** | The scope in which the instrument lies. | [optional] 
**instrument_uid** | **str** | The unique Lusid Instrument Id (LUID) of the instrument that this gain or loss is associated with. | 
**units** | **float** | The number of units of the associated instrument against which the gain or loss has been realised. | 
**purchase_trade_date** | **datetime** | The effective datetime at which the units associated with this gain or loss were originally purchased. | [optional] [readonly] 
**purchase_settlement_date** | **datetime** | The effective datetime at which the units associated with this gain or loss were originally settled. | [optional] [readonly] 
**purchase_price** | **float** | The purchase price of each unit associated with this gain or loss. | [optional] 
**cost_trade_ccy** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**cost_portfolio_ccy** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**realised_trade_ccy** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**realised_total** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**realised_market** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**realised_currency** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 

## Example

```python
from lusid.models.realised_gain_loss import RealisedGainLoss

# TODO update the JSON string below
json = "{}"
# create an instance of RealisedGainLoss from a JSON string
realised_gain_loss_instance = RealisedGainLoss.from_json(json)
# print the JSON string representation of the object
print RealisedGainLoss.to_json()

# convert the object into a dict
realised_gain_loss_dict = realised_gain_loss_instance.to_dict()
# create an instance of RealisedGainLoss from a dict
realised_gain_loss_form_dict = realised_gain_loss.from_dict(realised_gain_loss_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


