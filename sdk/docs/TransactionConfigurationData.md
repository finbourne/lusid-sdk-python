# TransactionConfigurationData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aliases** | [**List[TransactionConfigurationTypeAlias]**](TransactionConfigurationTypeAlias.md) | List of transaction types that map to this specific transaction configuration | 
**movements** | [**List[TransactionConfigurationMovementData]**](TransactionConfigurationMovementData.md) | Movement data for the transaction type | 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Properties attached to the transaction type | [optional] 
## Example

```python
from lusid.models.transaction_configuration_data import TransactionConfigurationData
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

aliases: List[TransactionConfigurationTypeAlias] = # Replace with your value
movements: List[TransactionConfigurationMovementData] = # Replace with your value
properties: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
transaction_configuration_data_instance = TransactionConfigurationData(aliases=aliases, movements=movements, properties=properties)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

