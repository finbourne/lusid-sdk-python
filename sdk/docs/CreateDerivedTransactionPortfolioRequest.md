# CreateDerivedTransactionPortfolioRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the derived transaction portfolio. | 
**description** | **str** | A description for the derived transaction portfolio. | [optional] 
**code** | **str** | The code of the derived transaction portfolio. Together with the scope this uniquely identifies the derived transaction portfolio. | 
**parent_portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**created** | **datetime** | This will be auto-populated to be the parent portfolio creation date. | [optional] 
**corporate_action_source_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**accounting_method** | **str** | . The available values are: Default, AverageCost, FirstInFirstOut, LastInFirstOut, HighestCostFirst, LowestCostFirst, ProRateByUnits, ProRateByCost, ProRateByCostPortfolioCurrency, IntraDayThenFirstInFirstOut, LongTermHighestCostFirst, LongTermHighestCostFirstPortfolioCurrency, HighestCostFirstPortfolioCurrency, LowestCostFirstPortfolioCurrency, MaximumLossMinimumGain, MaximumLossMinimumGainPortfolioCurrency | [optional] 
**sub_holding_keys** | **List[str]** | A set of unique transaction properties to group the derived transaction portfolio&#39;s holdings by, perhaps for strategy tagging. Each property must be from the &#39;Transaction&#39; domain and identified by a key in the format {domain}/{scope}/{code}, for example &#39;Transaction/strategies/quantsignal&#39;. See https://support.lusid.com/knowledgebase/article/KA-01879/en-us for more information. | [optional] 
**instrument_scopes** | **List[str]** | The resolution strategy used to resolve instruments of transactions/holdings upserted to this derived portfolio. | [optional] 
**amortisation_method** | **str** | The amortisation method used by the portfolio for the calculation. The available values are: NoAmortisation, StraightLine, EffectiveYield, StraightLineSettlementDate, EffectiveYieldSettlementDate | [optional] 
**transaction_type_scope** | **str** | The scope of the transaction types. | [optional] 
**cash_gain_loss_calculation_date** | **str** | The option when the Cash Gain Loss to be calulated, TransactionDate/SettlementDate. Defaults to SettlementDate. | [optional] 
**amortisation_rule_set_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**instrument_event_configuration** | [**InstrumentEventConfiguration**](InstrumentEventConfiguration.md) |  | [optional] 
## Example

```python
from lusid.models.create_derived_transaction_portfolio_request import CreateDerivedTransactionPortfolioRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr, validator
from datetime import datetime
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
code: StrictStr = "example_code"
parent_portfolio_id: ResourceId = # Replace with your value
created: Optional[datetime] = # Replace with your value
corporate_action_source_id: Optional[ResourceId] = # Replace with your value
accounting_method: Optional[StrictStr] = "example_accounting_method"
sub_holding_keys: Optional[conlist(StrictStr)] = # Replace with your value
instrument_scopes: Optional[conlist(StrictStr, max_items=1)] = Field(None, alias="instrumentScopes", description="The resolution strategy used to resolve instruments of transactions/holdings upserted to this derived portfolio.")
amortisation_method: Optional[StrictStr] = "example_amortisation_method"
transaction_type_scope: Optional[StrictStr] = "example_transaction_type_scope"
cash_gain_loss_calculation_date: Optional[StrictStr] = "example_cash_gain_loss_calculation_date"
amortisation_rule_set_id: Optional[ResourceId] = # Replace with your value
instrument_event_configuration: Optional[InstrumentEventConfiguration] = # Replace with your value
create_derived_transaction_portfolio_request_instance = CreateDerivedTransactionPortfolioRequest(display_name=display_name, description=description, code=code, parent_portfolio_id=parent_portfolio_id, created=created, corporate_action_source_id=corporate_action_source_id, accounting_method=accounting_method, sub_holding_keys=sub_holding_keys, instrument_scopes=instrument_scopes, amortisation_method=amortisation_method, transaction_type_scope=transaction_type_scope, cash_gain_loss_calculation_date=cash_gain_loss_calculation_date, amortisation_rule_set_id=amortisation_rule_set_id, instrument_event_configuration=instrument_event_configuration)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

