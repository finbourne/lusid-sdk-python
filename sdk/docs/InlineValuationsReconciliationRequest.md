# InlineValuationsReconciliationRequest

Specification for the reconciliation request. Left and Right hand sides are constructed. Each consists of a valuation of a inline set of instruments  using an inline aggregation request. The results of this can then be compared to each other. The difference, which is effectively a risk based  difference allows comparison of the effects of changing a recipe, valuation date, or (though it may or may not make logical sense) a set of instruments.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | [**InlineValuationRequest**](InlineValuationRequest.md) |  | 
**right** | [**InlineValuationRequest**](InlineValuationRequest.md) |  | 
**left_to_right_mapping** | [**List[ReconciliationLeftRightAddressKeyPair]**](ReconciliationLeftRightAddressKeyPair.md) | The mapping from property keys requested by left aggregation to property keys on right hand side | [optional] 
**preserve_keys** | **List[str]** | List of keys to preserve (from rhs) in the diff. Used in conjunction with filtering/grouping | [optional] 
## Example

```python
from lusid.models.inline_valuations_reconciliation_request import InlineValuationsReconciliationRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

left: InlineValuationRequest = # Replace with your value
right: InlineValuationRequest = # Replace with your value
left_to_right_mapping: Optional[conlist(ReconciliationLeftRightAddressKeyPair)] = # Replace with your value
preserve_keys: Optional[conlist(StrictStr)] = # Replace with your value
inline_valuations_reconciliation_request_instance = InlineValuationsReconciliationRequest(left=left, right=right, left_to_right_mapping=left_to_right_mapping, preserve_keys=preserve_keys)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

