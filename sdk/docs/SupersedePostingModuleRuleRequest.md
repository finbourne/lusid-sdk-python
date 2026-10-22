# SupersedePostingModuleRuleRequest

The next version of a Posting Rule, which takes over from its latest version on an accounting date
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_id** | **str** | The identifier of the Posting Rule. At most one rule in the request may have the ruleId of the superseded rule. If it does, the existing rule is capped so that it stops applying from this rule&#39;s EffectiveFrom, and this rule is created as its next version. Otherwise this rule is created as a new rule. | 
**effective_from** | **datetime** | The inclusive accounting date from which this rule applies. If this rule has the ruleId of the superseded rule, the superseded rule&#39;s latest version stops applying from this date, unless it already ends by then; it is never extended. | 
**effective_until** | **datetime** | The exclusive accounting date until which this rule applies. If not set, it applies until the end of time. | [optional] 
**general_ledger_account_code** | **str** | The general ledger account this rule posts the Activity credit or debit to. | 
**rule_filter** | **str** | The filter syntax for this rule. See https://support.lusid.com/docs/assigning-economic-activity-to-general-ledger-accounts-using-posting-rules for more information on filter syntax. | 
## Example

```python
from lusid.models.supersede_posting_module_rule_request import SupersedePostingModuleRuleRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

rule_id: StrictStr = "example_rule_id"
effective_from: datetime = # Replace with your value
effective_until: Optional[datetime] = # Replace with your value
general_ledger_account_code: StrictStr = "example_general_ledger_account_code"
rule_filter: StrictStr = "example_rule_filter"
supersede_posting_module_rule_request_instance = SupersedePostingModuleRuleRequest(rule_id=rule_id, effective_from=effective_from, effective_until=effective_until, general_ledger_account_code=general_ledger_account_code, rule_filter=rule_filter)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

