# TransactionTypeRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aliases** | [**List[TransactionTypeAlias]**](TransactionTypeAlias.md) | List of transaction types that map to this specific transaction configuration | 
**movements** | [**List[TransactionTypeMovement]**](TransactionTypeMovement.md) | Movement data for the transaction type | 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Properties attached to the transaction type | [optional] 
**calculations** | [**List[TransactionTypeCalculation]**](TransactionTypeCalculation.md) | Calculations to be performed for the transaction type | [optional] 
## Example

```python
from lusid.models.transaction_type_request import TransactionTypeRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist

aliases: conlist(TransactionTypeAlias) = # Replace with your value
movements: conlist(TransactionTypeMovement) = # Replace with your value
properties: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
calculations: Optional[conlist(TransactionTypeCalculation)] = # Replace with your value
transaction_type_request_instance = TransactionTypeRequest(aliases=aliases, movements=movements, properties=properties, calculations=calculations)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

