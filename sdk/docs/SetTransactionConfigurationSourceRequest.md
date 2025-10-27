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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

aliases: List[SetTransactionConfigurationAlias]
movements: List[TransactionConfigurationMovementDataRequest]
properties: Optional[Dict[str, PerpetualProperty]] = None
set_transaction_configuration_source_request_instance = SetTransactionConfigurationSourceRequest(aliases=aliases, movements=movements, properties=properties)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

