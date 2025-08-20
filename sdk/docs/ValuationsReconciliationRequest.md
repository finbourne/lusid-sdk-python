# ValuationsReconciliationRequest

Specification for the reconciliation request. Left and Right hand sides are constructed. Each consists of a valuation of a portfolio using an aggregation request. The results of this can then be compared to each other. The difference, which is effectively a risk based difference allows comparison of the effects of changing a recipe, valuation date, or (though it may or may not make logical sense) a portfolio. For instance, one might look at the difference in risk caused by the addition of transaction to a portfolio, or through changing the valuation methodology or system.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | [**ValuationRequest**](ValuationRequest.md) |  | 
**right** | [**ValuationRequest**](ValuationRequest.md) |  | 
**left_to_right_mapping** | [**List[ReconciliationLeftRightAddressKeyPair]**](ReconciliationLeftRightAddressKeyPair.md) | The mapping from property keys requested by left aggregation to property keys on right hand side | [optional] 
**preserve_keys** | **List[str]** | List of keys to preserve (from rhs) in the diff. Used in conjunction with filtering/grouping. If two values are equal, for a given key then the value is elided from the results. Setting it here will preserve it (takes the values from the RHS and puts it into the line by line results). | [optional] 
## Example

```python
from lusid.models.valuations_reconciliation_request import ValuationsReconciliationRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

left: ValuationRequest = # Replace with your value
right: ValuationRequest = # Replace with your value
left_to_right_mapping: Optional[conlist(ReconciliationLeftRightAddressKeyPair)] = # Replace with your value
preserve_keys: Optional[conlist(StrictStr)] = # Replace with your value
valuations_reconciliation_request_instance = ValuationsReconciliationRequest(left=left, right=right, left_to_right_mapping=left_to_right_mapping, preserve_keys=preserve_keys)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

