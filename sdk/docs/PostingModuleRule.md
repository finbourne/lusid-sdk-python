# PostingModuleRule

A Posting rule
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_id** | **str** | The identifier for the Posting Rule. | 
**general_ledger_account_code** | **str** | The general ledger account to post the Activity credit or debit to. | 
**rule_filter** | **str** | The filter syntax for the Posting Rule. See https://support.lusid.com/knowledgebase/article/KA-02140 for more information on filter syntax. | 
## Example

```python
from lusid.models.posting_module_rule import PostingModuleRule
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

rule_id: StrictStr = "example_rule_id"
general_ledger_account_code: StrictStr = "example_general_ledger_account_code"
rule_filter: StrictStr = "example_rule_filter"
posting_module_rule_instance = PostingModuleRule(rule_id=rule_id, general_ledger_account_code=general_ledger_account_code, rule_filter=rule_filter)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

