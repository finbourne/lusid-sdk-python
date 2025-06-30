# CleardownModuleRule

A Cleardown rule
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_id** | **str** | The identifier for the Cleardown Rule. | 
**general_ledger_account_code** | **str** | The account to post the residual P&amp;L to. | 
**rule_filter** | **str** | The filter syntax for the Cleardown Rule. See https://support.lusid.com/knowledgebase/article/KA-02140 for more information on filter syntax. | 
## Example

```python
from lusid.models.cleardown_module_rule import CleardownModuleRule
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr, validator

rule_id: StrictStr = "example_rule_id"
general_ledger_account_code: StrictStr = "example_general_ledger_account_code"
rule_filter: StrictStr = "example_rule_filter"
cleardown_module_rule_instance = CleardownModuleRule(rule_id=rule_id, general_ledger_account_code=general_ledger_account_code, rule_filter=rule_filter)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

