# BucketMembership

The bucket a Journal Entry Line was assigned to within one of a Fund Configuration's bucket sets.  Computed when the lines are read, from the bucket set definitions in force at that point.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_set_code** | **str** | The code of the bucket set that produced this classification. | [optional] 
**bucket_id** | **str** | The id of the bucket within that bucket set the line was assigned to, following the same first-match-wins waterfall used at valuation. One of the reserved &#39;_unmatched_dealing&#39;, &#39;_unmatched_fees&#39; or &#39;_unmatched_pnl&#39; ids when the line matched no bucket&#39;s filter in the set. | [optional] 
## Example

```python
from lusid.models.bucket_membership import BucketMembership
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

bucket_set_code: Optional[StrictStr] = "example_bucket_set_code"
bucket_id: Optional[StrictStr] = "example_bucket_id"
bucket_membership_instance = BucketMembership(bucket_set_code=bucket_set_code, bucket_id=bucket_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

