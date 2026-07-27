# BucketSetResult

A valuation point's results for one bucket set: whether the set is the apportionment set, and its per-node  (fund and share class) buckets and NAV. Allocation-group nodes are not included here - they are surfaced via  the apportionment results.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_apportionment** | **bool** | Whether this bucket set is the apportionment set (apportioning non-class-specific P&amp;L across share classes). | 
**nodes** | [**List[BucketSetNode]**](BucketSetNode.md) | The nodes making up the bucket set: the fund aggregate and one per share class. | 
## Example

```python
from lusid.models.bucket_set_result import BucketSetResult
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

is_apportionment: StrictBool = # Replace with your value
is_apportionment:StrictBool = True
nodes: List[BucketSetNode] = # Replace with your value
bucket_set_result_instance = BucketSetResult(is_apportionment=is_apportionment, nodes=nodes)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

