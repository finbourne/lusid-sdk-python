# PartnershipConfigPack

The partnership configuration pack a fund resolves to: the transaction types, chart of accounts and posting rules  the partners' ledger is booked under.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The scope of the configuration pack. | 
**code** | **str** | The code of the configuration pack. | 
**version** | **str** | The version of the configuration pack. | 
**transaction_types** | [**List[PackTransactionType]**](PackTransactionType.md) | The partnership transaction types the pack provides. | 
**chart_of_accounts** | [**List[PackAccount]**](PackAccount.md) | The accounts the pack posts partner capital to. | 
**posting_rules** | [**List[PackPostingRule]**](PackPostingRule.md) | The rules that move each transaction type between its accounts. | 
**general_ledger_profile_code** | **str** | The code of the general ledger profile the pack&#39;s posting rules belong to. | [optional] 
## Example

```python
from lusid.models.partnership_config_pack import PartnershipConfigPack
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

scope: StrictStr = "example_scope"
code: StrictStr = "example_code"
version: StrictStr = "example_version"
transaction_types: List[PackTransactionType] = # Replace with your value
chart_of_accounts: List[PackAccount] = # Replace with your value
posting_rules: List[PackPostingRule] = # Replace with your value
general_ledger_profile_code: Optional[StrictStr] = "example_general_ledger_profile_code"
partnership_config_pack_instance = PartnershipConfigPack(scope=scope, code=code, version=version, transaction_types=transaction_types, chart_of_accounts=chart_of_accounts, posting_rules=posting_rules, general_ledger_profile_code=general_ledger_profile_code)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

