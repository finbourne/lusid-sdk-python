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
**accounting_method** | **str** | . The available values are: Default, AverageCost, FirstInFirstOut, LastInFirstOut, HighestCostFirst, LowestCostFirst, ProRateByUnits, ProRateByCost, ProRateByCostPortfolioCurrency, IntraDayThenFirstInFirstOut, LongTermHighestCostFirst, LongTermHighestCostFirstPortfolioCurrency, HighestCostFirstPortfolioCurrency, LowestCostFirstPortfolioCurrency, MaximumLossMinimumGain, MaximumLossMinimumGainPortfolioCurrency | [optional] 
**amortisation_method** | **str** | The amortisation method used by the portfolio for the calculation. The available values are: NoAmortisation, StraightLine, EffectiveYield, StraightLineSettlementDate, EffectiveYieldSettlementDate | [optional] 
**transaction_type_scope** | **str** | The scope of the transaction types. | [optional] 
**cash_gain_loss_calculation_date** | **str** | The option when the Cash Gain Loss to be calulated, TransactionDate/SettlementDate. Defaults to SettlementDate. | [optional] 
**instrument_event_configuration** | [**InstrumentEventConfiguration**](InstrumentEventConfiguration.md) |  | [optional] 
**amortisation_rule_set_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**tax_rule_set_scope** | **str** | The scope of the tax rule sets for this portfolio. | [optional] 
**settlement_configuration** | [**PortfolioSettlementConfiguration**](PortfolioSettlementConfiguration.md) |  | [optional] 
**staged_modifications** | [**StagedModificationsInfo**](StagedModificationsInfo.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.portfolio_details import PortfolioDetails
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
origin_portfolio_id: ResourceId = # Replace with your value
version: Version
base_currency: StrictStr = "example_base_currency"
corporate_action_source_id: Optional[ResourceId] = # Replace with your value
sub_holding_keys: Optional[List[StrictStr]] = # Replace with your value
instrument_scopes: Optional[List[StrictStr]] = # Replace with your value
accounting_method: Optional[StrictStr] = "example_accounting_method"
amortisation_method: Optional[StrictStr] = "example_amortisation_method"
transaction_type_scope: Optional[StrictStr] = "example_transaction_type_scope"
cash_gain_loss_calculation_date: Optional[StrictStr] = "example_cash_gain_loss_calculation_date"
instrument_event_configuration: Optional[InstrumentEventConfiguration] = # Replace with your value
amortisation_rule_set_id: Optional[ResourceId] = # Replace with your value
tax_rule_set_scope: Optional[StrictStr] = "example_tax_rule_set_scope"
settlement_configuration: Optional[PortfolioSettlementConfiguration] = # Replace with your value
staged_modifications: Optional[StagedModificationsInfo] = # Replace with your value
links: Optional[List[Link]] = None
portfolio_details_instance = PortfolioDetails(href=href, origin_portfolio_id=origin_portfolio_id, version=version, base_currency=base_currency, corporate_action_source_id=corporate_action_source_id, sub_holding_keys=sub_holding_keys, instrument_scopes=instrument_scopes, accounting_method=accounting_method, amortisation_method=amortisation_method, transaction_type_scope=transaction_type_scope, cash_gain_loss_calculation_date=cash_gain_loss_calculation_date, instrument_event_configuration=instrument_event_configuration, amortisation_rule_set_id=amortisation_rule_set_id, tax_rule_set_scope=tax_rule_set_scope, settlement_configuration=settlement_configuration, staged_modifications=staged_modifications, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

