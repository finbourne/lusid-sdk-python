# UpsertInvestor

Inner dto of an Investor Record on the LUSID API
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**investor_type** | **str** | The type of the Investor | [optional] 
**investor_identifiers** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The identifiers of the Investor | [optional] 
## Example

```python
from lusid.models.upsert_investor import UpsertInvestor
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr

investor_type: Optional[StrictStr] = "example_investor_type"
investor_identifiers: Optional[Dict[str, ModelProperty]] = # Replace with your value
upsert_investor_instance = UpsertInvestor(investor_type=investor_type, investor_identifiers=investor_identifiers)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

