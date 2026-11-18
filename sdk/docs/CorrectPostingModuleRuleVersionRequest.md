# CorrectPostingModuleRuleVersionRequest

The corrected content of one version of a Posting Rule. The version keeps its rule identifier and version number.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**general_ledger_account_code** | **str** | The general ledger account this version of the rule posts the Activity credit or debit to. | 
**rule_filter** | **str** | The filter syntax for this version of the rule. See https://support.lusid.com/docs/assigning-economic-activity-to-general-ledger-accounts-using-posting-rules for more information on filter syntax. | 
**effective_from** | **datetime** | The inclusive accounting date from which this version of the rule applies. If not set, it applies from the beginning of time. | [optional] 
**effective_until** | **datetime** | The exclusive accounting date until which this version of the rule applies. If not set, it applies until the end of time. | [optional] 
## Example

```python
from lusid.models.correct_posting_module_rule_version_request import CorrectPostingModuleRuleVersionRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

general_ledger_account_code: StrictStr = "example_general_ledger_account_code"
rule_filter: StrictStr = "example_rule_filter"
effective_from: Optional[datetime] = # Replace with your value
effective_until: Optional[datetime] = # Replace with your value
correct_posting_module_rule_version_request_instance = CorrectPostingModuleRuleVersionRequest(general_ledger_account_code=general_ledger_account_code, rule_filter=rule_filter, effective_from=effective_from, effective_until=effective_until)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

