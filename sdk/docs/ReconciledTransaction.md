# ReconciledTransaction

Information about reconciled transactions.  At least one of Finbourne.WebApi.Interface.Dto.Reconciliation.ReconciledTransaction.Left and Finbourne.WebApi.Interface.Dto.Reconciliation.ReconciledTransaction.Right will be populated.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | [**Transaction**](Transaction.md) |  | [optional] 
**right** | [**Transaction**](Transaction.md) |  | [optional] 
**percentage_match** | **float** | How good a match this is considered to be. | [optional] 
**mapping_rule_set_results** | **List[bool]** | The result of each individual mapping rule result.  Will only be present if both Finbourne.WebApi.Interface.Dto.Reconciliation.ReconciledTransaction.Left and Finbourne.WebApi.Interface.Dto.Reconciliation.ReconciledTransaction.Right are populated. | [optional] 
## Example

```python
from lusid.models.reconciled_transaction import ReconciledTransaction
from typing import Any, Dict, List, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictBool, StrictFloat, StrictInt, conlist

left: Optional[Transaction] = None
right: Optional[Transaction] = None
percentage_match: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
mapping_rule_set_results: Optional[conlist(StrictBool)] = # Replace with your value
reconciled_transaction_instance = ReconciledTransaction(left=left, right=right, percentage_match=percentage_match, mapping_rule_set_results=mapping_rule_set_results)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

