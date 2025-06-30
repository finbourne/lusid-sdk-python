# SetTransactionConfigurationSourceRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aliases** | [**List[SetTransactionConfigurationAlias]**](SetTransactionConfigurationAlias.md) |  | 
**movements** | [**List[TransactionConfigurationMovementDataRequest]**](TransactionConfigurationMovementDataRequest.md) |  | 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) |  | [optional] 
## Example

```python
from lusid.models.set_transaction_configuration_source_request import SetTransactionConfigurationSourceRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist

aliases: conlist(SetTransactionConfigurationAlias) = # Replace with your value
movements: conlist(TransactionConfigurationMovementDataRequest) = # Replace with your value
properties: Optional[Dict[str, PerpetualProperty]] = None
set_transaction_configuration_source_request_instance = SetTransactionConfigurationSourceRequest(aliases=aliases, movements=movements, properties=properties)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

