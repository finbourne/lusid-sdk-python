# AccountHolderIdentifier

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A client-defined key used to identify the Account Holder, unique within the Investment Account | 
**scope** | **str** | The scope in which the Investor Record lies. | 
**identifiers** | [**Dict[str, ModelProperty]**](ModelProperty.md) | Single Account Holder identifier that should target the desired Investor Record. | 
## Example

```python
from lusid.models.account_holder_identifier import AccountHolderIdentifier
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr, validator

key: StrictStr = "example_key"
scope: StrictStr = "example_scope"
identifiers: Dict[str, ModelProperty] = # Replace with your value
account_holder_identifier_instance = AccountHolderIdentifier(key=key, scope=scope, identifiers=identifiers)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

