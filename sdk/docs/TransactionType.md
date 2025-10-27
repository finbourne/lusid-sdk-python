# TransactionType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aliases** | [**List[TransactionTypeAlias]**](TransactionTypeAlias.md) | List of transaction types that map to this specific transaction configuration | 
**movements** | [**List[TransactionTypeMovement]**](TransactionTypeMovement.md) | Movement data for the transaction type | 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Properties attached to the transaction type | [optional] 
**calculations** | [**List[TransactionTypeCalculation]**](TransactionTypeCalculation.md) | Calculations to be performed for the transaction type | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.transaction_type import TransactionType
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

aliases: List[TransactionTypeAlias] = # Replace with your value
movements: List[TransactionTypeMovement] = # Replace with your value
properties: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
calculations: Optional[List[TransactionTypeCalculation]] = # Replace with your value
links: Optional[List[Link]] = None
transaction_type_instance = TransactionType(aliases=aliases, movements=movements, properties=properties, calculations=calculations, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

