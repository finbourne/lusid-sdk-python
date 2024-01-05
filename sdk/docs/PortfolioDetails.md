# PortfolioDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**origin_portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**version** | [**Version**](Version.md) |  | 
**base_currency** | **str** | The base currency of the transaction portfolio. | 
**corporate_action_source_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**sub_holding_keys** | **List[str]** |  | [optional] 
**instrument_scopes** | **List[str]** | The resolution strategy used to resolve instruments of transactions/holdings upserted to the transaction portfolio. | [optional] 
**accounting_method** | **str** | . The available values are: Default, AverageCost, FirstInFirstOut, LastInFirstOut, HighestCostFirst, LowestCostFirst | [optional] 
**amortisation_method** | **str** | The amortisation method used by the portfolio for the calculation. The available values are: NoAmortisation, StraightLine, EffectiveYield, StraightLineSettlementDate, EffectiveYieldSettlementDate | [optional] 
**transaction_type_scope** | **str** | The scope of the transaction types. | [optional] 
**cash_gain_loss_calculation_date** | **str** | The option when the Cash Gain Loss to be calulated, TransactionDate/SettlementDate. Defaults to SettlementDate. | [optional] 
**instrument_event_configuration** | [**InstrumentEventConfiguration**](InstrumentEventConfiguration.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.portfolio_details import PortfolioDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PortfolioDetails from a JSON string
portfolio_details_instance = PortfolioDetails.from_json(json)
# print the JSON string representation of the object
print PortfolioDetails.to_json()

# convert the object into a dict
portfolio_details_dict = portfolio_details_instance.to_dict()
# create an instance of PortfolioDetails from a dict
portfolio_details_form_dict = portfolio_details.from_dict(portfolio_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


