# TransactionConfigurationDataRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aliases** | [**List[TransactionConfigurationTypeAlias]**](TransactionConfigurationTypeAlias.md) | List of transaction codes that map to this specific transaction model | 
**movements** | [**List[TransactionConfigurationMovementDataRequest]**](TransactionConfigurationMovementDataRequest.md) | Movement data for the transaction code | 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Properties attached to the underlying holding. | [optional] 
## Example

```python
from lusid.models.transaction_configuration_data_request import TransactionConfigurationDataRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

aliases: List[TransactionConfigurationTypeAlias] = # Replace with your value
movements: List[TransactionConfigurationMovementDataRequest] = # Replace with your value
properties: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
transaction_configuration_data_request_instance = TransactionConfigurationDataRequest(aliases=aliases, movements=movements, properties=properties)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

