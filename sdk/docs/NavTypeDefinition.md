# NavTypeDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**chart_of_accounts_id** | [**ResourceId**](ResourceId.md) |  | 
**posting_module_codes** | **List[str]** |  | [optional] 
**cleardown_module_codes** | **List[str]** |  | [optional] 
**valuation_recipe_id** | [**ResourceId**](ResourceId.md) |  | 
**holding_recipe_id** | [**ResourceId**](ResourceId.md) |  | 
**accounting_method** | **str** |  | 
**sub_holding_keys** | **List[str]** | Set of unique holding identifiers, e.g. trader, desk, strategy. | [optional] 
**amortisation_method** | **str** |  | 
**transaction_type_scope** | **str** |  | 
**cash_gain_loss_calculation_date** | **str** |  | 
**amortisation_rule_set_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**leader_nav_type_code** | **str** |  | [optional] 
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
valuation_recipe_id: ResourceId = # Replace with your value
holding_recipe_id: ResourceId = # Replace with your value
accounting_method: StrictStr = "example_accounting_method"
sub_holding_keys: Optional[List[StrictStr]] = # Replace with your value
amortisation_method: StrictStr = "example_amortisation_method"
transaction_type_scope: StrictStr = "example_transaction_type_scope"
cash_gain_loss_calculation_date: StrictStr = "example_cash_gain_loss_calculation_date"
amortisation_rule_set_id: Optional[ResourceId] = # Replace with your value
leader_nav_type_code: Optional[StrictStr] = "example_leader_nav_type_code"
nav_type_definition_instance = NavTypeDefinition(code=code, display_name=display_name, description=description, chart_of_accounts_id=chart_of_accounts_id, posting_module_codes=posting_module_codes, cleardown_module_codes=cleardown_module_codes, valuation_recipe_id=valuation_recipe_id, holding_recipe_id=holding_recipe_id, accounting_method=accounting_method, sub_holding_keys=sub_holding_keys, amortisation_method=amortisation_method, transaction_type_scope=transaction_type_scope, cash_gain_loss_calculation_date=cash_gain_loss_calculation_date, amortisation_rule_set_id=amortisation_rule_set_id, leader_nav_type_code=leader_nav_type_code)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

