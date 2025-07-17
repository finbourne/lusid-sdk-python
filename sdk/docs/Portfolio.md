# Portfolio

A list of portfolios.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
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
**tax_rule_set_scope** | **str** | The scope of the tax rule sets for this portfolio. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.portfolio import Portfolio
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr, conlist, constr, validator
from datetime import datetime
href: Optional[StrictStr] = "example_href"
id: ResourceId = # Replace with your value
type: StrictStr = "example_type"
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
created: datetime = # Replace with your value
parent_portfolio_id: Optional[ResourceId] = # Replace with your value
version: Optional[Version] = None
staged_modifications: Optional[StagedModificationsInfo] = # Replace with your value
is_derived: Optional[StrictBool] = # Replace with your value
is_derived:Optional[StrictBool] = None
base_currency: Optional[StrictStr] = "example_base_currency"
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
relationships: Optional[conlist(Relationship)] = # Replace with your value
instrument_scopes: Optional[conlist(StrictStr)] = # Replace with your value
accounting_method: Optional[StrictStr] = "example_accounting_method"
amortisation_method: Optional[StrictStr] = "example_amortisation_method"
transaction_type_scope: Optional[StrictStr] = "example_transaction_type_scope"
cash_gain_loss_calculation_date: Optional[StrictStr] = "example_cash_gain_loss_calculation_date"
instrument_event_configuration: Optional[InstrumentEventConfiguration] = # Replace with your value
amortisation_rule_set_id: Optional[ResourceId] = # Replace with your value
tax_rule_set_scope: Optional[StrictStr] = "example_tax_rule_set_scope"
links: Optional[conlist(Link)] = None
portfolio_instance = Portfolio(href=href, id=id, type=type, display_name=display_name, description=description, created=created, parent_portfolio_id=parent_portfolio_id, version=version, staged_modifications=staged_modifications, is_derived=is_derived, base_currency=base_currency, properties=properties, relationships=relationships, instrument_scopes=instrument_scopes, accounting_method=accounting_method, amortisation_method=amortisation_method, transaction_type_scope=transaction_type_scope, cash_gain_loss_calculation_date=cash_gain_loss_calculation_date, instrument_event_configuration=instrument_event_configuration, amortisation_rule_set_id=amortisation_rule_set_id, tax_rule_set_scope=tax_rule_set_scope, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

