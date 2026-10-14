# PackPostingRule

A posting rule on a partnership configuration pack.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_id** | **str** | The posting rule identifier. | 
**transaction_type** | **str** | The transaction type. | 
**debit_account** | **str** | The account debited. | 
**credit_account** | **str** | The account credited. | 
## Example

```python
from lusid.models.pack_posting_rule import PackPostingRule
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

rule_id: StrictStr = "example_rule_id"
transaction_type: StrictStr = "example_transaction_type"
debit_account: StrictStr = "example_debit_account"
credit_account: StrictStr = "example_credit_account"
pack_posting_rule_instance = PackPostingRule(rule_id=rule_id, transaction_type=transaction_type, debit_account=debit_account, credit_account=credit_account)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

