# BucketSetSeedRequest

The closing balances to seed for a bucket set on an estimate valuation point.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_set_code** | **str** | The code of the bucket set on the fund configuration to seed. | 
**class_seeds** | [**List[BucketSetClassSeedRequest]**](BucketSetClassSeedRequest.md) | The bucket set&#39;s closing balances at the valuation point, per share class. They replace everything the bucket set holds up to and including the valuation point. A share class or bucket left out is zero. | 
## Example

```python
from lusid.models.bucket_set_seed_request import BucketSetSeedRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

bucket_set_code: StrictStr = "example_bucket_set_code"
class_seeds: List[BucketSetClassSeedRequest] = # Replace with your value
bucket_set_seed_request_instance = BucketSetSeedRequest(bucket_set_code=bucket_set_code, class_seeds=class_seeds)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

