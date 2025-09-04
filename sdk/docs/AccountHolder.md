# AccountHolder

An Account Holder of an Investment Account.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A client-defined key used to identify the Account Holder, unique within the Investment Account | [optional] 
**scope** | **str** | The scope in which the Investor Record lies. | [optional] 
**identifiers** | **Dict[str, str]** | Single Account Holder identifier that should target the desired Investor Record. | [optional] 
**entity_unique_id** | **str** | The unique InvestorRecord entity identifier | [optional] 
**investor_record** | [**InvestorRecord**](InvestorRecord.md) |  | [optional] 
## Example

```python
from lusid.models.account_holder import AccountHolder
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr

key: Optional[StrictStr] = "example_key"
scope: Optional[StrictStr] = "example_scope"
identifiers: Optional[Dict[str, StrictStr]] = # Replace with your value
entity_unique_id: Optional[StrictStr] = "example_entity_unique_id"
investor_record: Optional[InvestorRecord] = # Replace with your value
account_holder_instance = AccountHolder(key=key, scope=scope, identifiers=identifiers, entity_unique_id=entity_unique_id, investor_record=investor_record)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

