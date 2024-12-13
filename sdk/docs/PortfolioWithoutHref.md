# PortfolioWithoutHref

A list of portfolios.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**type** | **str** | The type of the portfolio. The available values are: Transaction, Reference, DerivedTransaction, SimplePosition | 
**display_name** | **str** | The name of the portfolio. | 
**description** | **str** | The long form description of the portfolio. | [optional] 
**created** | **datetime** | The effective datetime at which the portfolio was created. No transactions or constituents can be added to the portfolio before this date. | 
**parent_portfolio_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**staged_modifications** | [**StagedModificationsInfo**](StagedModificationsInfo.md) |  | [optional] 
**is_derived** | **bool** | Whether or not this is a derived portfolio. | [optional] 
**base_currency** | **str** | The base currency of the portfolio. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The requested portfolio properties. These will be from the &#39;Portfolio&#39; domain. | [optional] 
**relationships** | [**List[Relationship]**](Relationship.md) | A set of relationships associated to the portfolio. | [optional] 
**instrument_scopes** | **List[str]** | The instrument scope resolution strategy of this portfolio. | [optional] 
**accounting_method** | **str** | . The available values are: Default, AverageCost, FirstInFirstOut, LastInFirstOut, HighestCostFirst, LowestCostFirst, ProRateByUnits, ProRateByCost, ProRateByCostPortfolioCurrency, IntraDayThenFirstInFirstOut, LongTermHighestCostFirst, LongTermHighestCostFirstPortfolioCurrency, HighestCostFirstPortfolioCurrency, LowestCostFirstPortfolioCurrency, MaximumLossMinimumGain, MaximumLossMinimumGainPortfolioCurrency | [optional] 
**amortisation_method** | **str** | The amortisation method used by the portfolio for the calculation. The available values are: NoAmortisation, StraightLine, EffectiveYield, StraightLineSettlementDate, EffectiveYieldSettlementDate | [optional] 
**transaction_type_scope** | **str** | The scope of the transaction types. | [optional] 
**cash_gain_loss_calculation_date** | **str** | The scope of the transaction types. | [optional] 
**instrument_event_configuration** | [**InstrumentEventConfiguration**](InstrumentEventConfiguration.md) |  | [optional] 
**amortisation_rule_set_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.portfolio_without_href import PortfolioWithoutHref

# TODO update the JSON string below
json = "{}"
# create an instance of PortfolioWithoutHref from a JSON string
portfolio_without_href_instance = PortfolioWithoutHref.from_json(json)
# print the JSON string representation of the object
print PortfolioWithoutHref.to_json()

# convert the object into a dict
portfolio_without_href_dict = portfolio_without_href_instance.to_dict()
# create an instance of PortfolioWithoutHref from a dict
portfolio_without_href_form_dict = portfolio_without_href.from_dict(portfolio_without_href_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


