# RecLinkedResult

A rec result of a different rec type in the same rec instance whose items share an identifier with this  result's items, and the keys that established the link. Links are symmetric: the linked result carries one back.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the linked result, as carried in that result&#39;s own id field. | 
**rec_type** | **str** | The rec type of the linked result. Always differs from this result&#39;s rec type. Available values: Holding, CashHolding, Valuation, InputTransaction, OutputTransaction, SettlementActivity. | 
**linked_by** | [**RecLinkedBy**](RecLinkedBy.md) |  | 
## Example

```python
from lusid.models.rec_linked_result import RecLinkedResult
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: StrictStr = "example_id"
rec_type: StrictStr = "example_rec_type"
linked_by: RecLinkedBy = # Replace with your value
rec_linked_result_instance = RecLinkedResult(id=id, rec_type=rec_type, linked_by=linked_by)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

