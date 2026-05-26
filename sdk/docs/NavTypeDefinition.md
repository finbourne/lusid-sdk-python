# NavTypeDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The Code for the Nav Type. Must be unique within the Fund. | [optional] 
**display_name** | **str** | The Display Name for the Nav Type. Must be unique within the Fund. | [optional] 
**description** | **str** | The Description for the Nav Type. | [optional] 
**chart_of_accounts_id** | [**ResourceId**](ResourceId.md) |  | 
**posting_module_codes** | **List[str]** | The Posting Module Codes from which the rules to be applied are retrieved. | [optional] 
**cleardown_module_codes** | **List[str]** | The Cleardown Module Codes from which the rules to be applied are retrieved. | [optional] 
**settlement_configuration** | [**NavSettlementConfiguration**](NavSettlementConfiguration.md) |  | [optional] 
**valuation_recipe_id** | [**ResourceId**](ResourceId.md) |  | 
**holding_recipe_id** | [**ResourceId**](ResourceId.md) |  | 
**accounting_method** | **str** | Determines the accounting treatment given to the simple position portfolio&#39;s tax lots. A non-default value is required. Available values: AverageCost, FirstInFirstOut, LastInFirstOut, HighestCostFirst, LowestCostFirst, ProRateByUnits, ProRateByCost, ProRateByCostPortfolioCurrency, IntraDayThenFirstInFirstOut, LongTermHighestCostFirst, LongTermHighestCostFirstPortfolioCurrency, HighestCostFirstPortfolioCurrency, LowestCostFirstPortfolioCurrency, MaximumLossMinimumGain, MaximumLossMinimumGainPortfolioCurrency. | 
**sub_holding_keys** | **List[str]** | A set of unique transaction properties to group the derived transaction portfolio&#39;s holdings by, perhaps for strategy tagging. Each property must be from the &#39;Transaction&#39; domain and identified by a key in the format {domain}/{scope}/{code}, for example &#39;Transaction/strategies/quantsignal&#39;. See https://support.lusid.com/knowledgebase/article/KA-01879/en-us for more information. | [optional] 
**amortisation_method** | **str** | The amortisation method used by the portfolio for the calculation. Available values: NoAmortisation, StraightLine, EffectiveYield, StraightLineSettlementDate, EffectiveYieldSettlementDate. | 
**transaction_type_scope** | **str** | The scope of the transaction types. | 
**cash_gain_loss_calculation_date** | **str** | The option when the Cash Gain Loss to be calulated, TransactionDate/SettlementDate. A non-default value is required. Available values: SettlementDate, TransactionDate. | 
**amortisation_rule_set_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**leader_nav_type_code** | **str** | The code of the Nav Type that this Nav Type will follow when set. | [optional] 
**transaction_template_scope** | **str** | The Transaction Template Scope used by the NavType. Will default to the scope set on the parent portfolio. If the fund has multiple parent portfolios, then the Transaction Template Scope must be provided. | [optional] 
## Example

```python
from lusid.models.nav_type_definition import NavTypeDefinition
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

code: Optional[StrictStr] = "example_code"
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
chart_of_accounts_id: ResourceId = # Replace with your value
posting_module_codes: Optional[List[StrictStr]] = # Replace with your value
cleardown_module_codes: Optional[List[StrictStr]] = # Replace with your value
settlement_configuration: Optional[NavSettlementConfiguration] = # Replace with your value
valuation_recipe_id: ResourceId = # Replace with your value
holding_recipe_id: ResourceId = # Replace with your value
accounting_method: StrictStr = "example_accounting_method"
sub_holding_keys: Optional[List[StrictStr]] = # Replace with your value
amortisation_method: StrictStr = "example_amortisation_method"
transaction_type_scope: StrictStr = "example_transaction_type_scope"
cash_gain_loss_calculation_date: StrictStr = "example_cash_gain_loss_calculation_date"
amortisation_rule_set_id: Optional[ResourceId] = # Replace with your value
leader_nav_type_code: Optional[StrictStr] = "example_leader_nav_type_code"
transaction_template_scope: Optional[StrictStr] = "example_transaction_template_scope"
nav_type_definition_instance = NavTypeDefinition(code=code, display_name=display_name, description=description, chart_of_accounts_id=chart_of_accounts_id, posting_module_codes=posting_module_codes, cleardown_module_codes=cleardown_module_codes, settlement_configuration=settlement_configuration, valuation_recipe_id=valuation_recipe_id, holding_recipe_id=holding_recipe_id, accounting_method=accounting_method, sub_holding_keys=sub_holding_keys, amortisation_method=amortisation_method, transaction_type_scope=transaction_type_scope, cash_gain_loss_calculation_date=cash_gain_loss_calculation_date, amortisation_rule_set_id=amortisation_rule_set_id, leader_nav_type_code=leader_nav_type_code, transaction_template_scope=transaction_template_scope)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

