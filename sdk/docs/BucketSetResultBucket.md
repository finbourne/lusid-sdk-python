# BucketSetResultBucket

One bucket's values within a bucket set node: the movement in the period plus the cumulative values before  and after it (CumulativeValue = Value + PreviousCumulativeValue).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_id** | **str** | The identifier of the bucket. | 
**bucket_type** | **str** | The type of the bucket (for example Dealing or PnL). | 
**value** | **float** | The movement in the bucket over the valuation point&#39;s period. | 
**previous_cumulative_value** | **float** | The cumulative value of the bucket up to the start of the period. | 
**cumulative_value** | **float** | The cumulative value of the bucket up to the end of the period (Value + PreviousCumulativeValue). | 
## Example

```python
from lusid.models.bucket_set_result_bucket import BucketSetResultBucket
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

bucket_id: StrictStr = "example_bucket_id"
bucket_type: StrictStr = "example_bucket_type"
value: Union[StrictFloat, StrictInt] = # Replace with your value
previous_cumulative_value: Union[StrictFloat, StrictInt] = # Replace with your value
cumulative_value: Union[StrictFloat, StrictInt] = # Replace with your value
bucket_set_result_bucket_instance = BucketSetResultBucket(bucket_id=bucket_id, bucket_type=bucket_type, value=value, previous_cumulative_value=previous_cumulative_value, cumulative_value=cumulative_value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

