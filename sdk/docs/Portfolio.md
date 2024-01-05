# Portfolio

A list of portfolios.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | 
**type** | **str** | The type of the portfolio. The available values are: Transaction, Reference, DerivedTransaction | 
**display_name** | **str** | The name of the portfolio. | 
**description** | **str** | The long form description of the portfolio. | [optional] 
**created** | **datetime** | The effective datetime at which the portfolio was created. No transactions or constituents can be added to the portfolio before this date. | 
**parent_portfolio_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**is_derived** | **bool** | Whether or not this is a derived portfolio. | [optional] 
**base_currency** | **str** | The base currency of the portfolio. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The requested portfolio properties. These will be from the &#39;Portfolio&#39; domain. | [optional] 
**relationships** | [**List[Relationship]**](Relationship.md) | A set of relationships associated to the portfolio. | [optional] 
**instrument_scopes** | **List[str]** | The instrument scope resolution strategy of this portfolio. | [optional] 
**accounting_method** | **str** | . The available values are: Default, AverageCost, FirstInFirstOut, LastInFirstOut, HighestCostFirst, LowestCostFirst | [optional] 
**amortisation_method** | **str** | The amortisation method used by the portfolio for the calculation. The available values are: NoAmortisation, StraightLine, EffectiveYield, StraightLineSettlementDate, EffectiveYieldSettlementDate | [optional] 
**transaction_type_scope** | **str** | The scope of the transaction types. | [optional] 
**cash_gain_loss_calculation_date** | **str** | The scope of the transaction types. | [optional] 
**instrument_event_configuration** | [**InstrumentEventConfiguration**](InstrumentEventConfiguration.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.portfolio import Portfolio

# TODO update the JSON string below
json = "{}"
# create an instance of Portfolio from a JSON string
portfolio_instance = Portfolio.from_json(json)
# print the JSON string representation of the object
print Portfolio.to_json()

# convert the object into a dict
portfolio_dict = portfolio_instance.to_dict()
# create an instance of Portfolio from a dict
portfolio_form_dict = portfolio.from_dict(portfolio_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


