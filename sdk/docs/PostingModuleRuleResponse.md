# PostingModuleRuleResponse

A version of a Posting rule
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_id** | **str** | The identifier for the Posting Rule. | 
**general_ledger_account_code** | **str** | The general ledger account to post the Activity credit or debit to. | 
**rule_filter** | **str** | The filter syntax for the Posting Rule. See https://support.lusid.com/docs/assigning-economic-activity-to-general-ledger-accounts-using-posting-rules for more information on filter syntax. | 
**effective_from** | **datetime** | The inclusive accounting date from which the Posting Rule applies. If not set, the rule applies from the beginning of time. | [optional] 
**effective_until** | **datetime** | The exclusive accounting date until which the Posting Rule applies. If not set, the rule applies until the end of time. | [optional] 
**version** | **int** | The version of the Posting Rule. Starts at 1 and increases each time the rule is superseded. | [optional] 
**original_rule_id** | **str** | The identifier of the Posting Rule that this rule was created to supersede, if any. | [optional] 
## Example

```python
from lusid.models.posting_module_rule_response import PostingModuleRuleResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

rule_id: StrictStr = "example_rule_id"
general_ledger_account_code: StrictStr = "example_general_ledger_account_code"
rule_filter: StrictStr = "example_rule_filter"
effective_from: Optional[datetime] = # Replace with your value
effective_until: Optional[datetime] = # Replace with your value
version: Optional[StrictInt] = # Replace with your value
version: Optional[StrictInt] = None
original_rule_id: Optional[StrictStr] = "example_original_rule_id"
posting_module_rule_response_instance = PostingModuleRuleResponse(rule_id=rule_id, general_ledger_account_code=general_ledger_account_code, rule_filter=rule_filter, effective_from=effective_from, effective_until=effective_until, version=version, original_rule_id=original_rule_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

