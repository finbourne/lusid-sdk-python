# ReconciliationLeftRightAddressKeyPair

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | **str** | Address key defined by the lhs aggregation | 
**right** | **str** | Address key defined by the rhs aggregation | 
## Example

```python
from lusid.models.reconciliation_left_right_address_key_pair import ReconciliationLeftRightAddressKeyPair
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, StrictStr

left: StrictStr = "example_left"
right: StrictStr = "example_right"
reconciliation_left_right_address_key_pair_instance = ReconciliationLeftRightAddressKeyPair(left=left, right=right)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

