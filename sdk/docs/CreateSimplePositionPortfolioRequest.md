# CreateSimplePositionPortfolioRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the simple position portfolio. | 
**description** | **str** | A description for the simple position portfolio. | [optional] 
**code** | **str** | The code of the simple position portfolio. Together with the scope this uniquely identifies the simple position portfolio. | 
**created** | **datetime** | The effective datetime at which to create the simple position portfolio. No holdings can be set on the simple position portfolio before this date. Defaults to the current LUSID system datetime if not specified. | [optional] 
**base_currency** | **str** | The base currency of the simple position portfolio in ISO 4217 currency code format. | 
**corporate_action_source_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**accounting_method** | **str** | . The available values are: Default, AverageCost, FirstInFirstOut, LastInFirstOut, HighestCostFirst, LowestCostFirst, ProRateByUnits, ProRateByCost, ProRateByCostPortfolioCurrency, IntraDayThenFirstInFirstOut, LongTermHighestCostFirst, LongTermHighestCostFirstPortfolioCurrency, HighestCostFirstPortfolioCurrency, LowestCostFirstPortfolioCurrency, MaximumLossMinimumGain, MaximumLossMinimumGainPortfolioCurrency | [optional] 
**sub_holding_keys** | **List[str]** | A set of unique transaction properties to group the simple position portfolio&#39;s holdings by, perhaps for strategy tagging. Each property must be from the &#39;Transaction&#39; domain and identified by a key in the format {domain}/{scope}/{code}, for example &#39;Transaction/strategies/quantsignal&#39;. See https://support.lusid.com/knowledgebase/article/KA-01879/en-us for more information. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of unique portfolio properties to add custom data to the simple position portfolio. Each property must be from the &#39;Portfolio&#39; domain and identified by a key in the format {domain}/{scope}/{code}, for example &#39;Portfolio/Manager/Id&#39;. Note these properties must be pre-defined. | [optional] 
**instrument_scopes** | **List[str]** | The resolution strategy used to resolve instruments of holdings upserted to this portfolio. | [optional] 
**amortisation_method** | **str** | The amortisation method used by the portfolio for the calculation. The available values are: NoAmortisation, StraightLine, EffectiveYield, StraightLineSettlementDate, EffectiveYieldSettlementDate | [optional] 
**transaction_type_scope** | **str** | The scope of the transaction types. | [optional] 
**cash_gain_loss_calculation_date** | **str** | The option when the Cash Gain Loss to be calulated, TransactionDate/SettlementDate. Defaults to SettlementDate. | [optional] 
**instrument_event_configuration** | [**InstrumentEventConfiguration**](InstrumentEventConfiguration.md) |  | [optional] 
**amortisation_rule_set_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
## Example

```python
from lusid.models.create_simple_position_portfolio_request import CreateSimplePositionPortfolioRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
code: StrictStr = "example_code"
created: Optional[datetime] = # Replace with your value
base_currency: StrictStr = "example_base_currency"
corporate_action_source_id: Optional[ResourceId] = # Replace with your value
accounting_method: Optional[StrictStr] = "example_accounting_method"
sub_holding_keys: Optional[List[StrictStr]] = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
instrument_scopes: Optional[List[StrictStr]] = # Replace with your value
amortisation_method: Optional[StrictStr] = "example_amortisation_method"
transaction_type_scope: Optional[StrictStr] = "example_transaction_type_scope"
cash_gain_loss_calculation_date: Optional[StrictStr] = "example_cash_gain_loss_calculation_date"
instrument_event_configuration: Optional[InstrumentEventConfiguration] = # Replace with your value
amortisation_rule_set_id: Optional[ResourceId] = # Replace with your value
create_simple_position_portfolio_request_instance = CreateSimplePositionPortfolioRequest(display_name=display_name, description=description, code=code, created=created, base_currency=base_currency, corporate_action_source_id=corporate_action_source_id, accounting_method=accounting_method, sub_holding_keys=sub_holding_keys, properties=properties, instrument_scopes=instrument_scopes, amortisation_method=amortisation_method, transaction_type_scope=transaction_type_scope, cash_gain_loss_calculation_date=cash_gain_loss_calculation_date, instrument_event_configuration=instrument_event_configuration, amortisation_rule_set_id=amortisation_rule_set_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

