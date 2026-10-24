# BucketSetClassSeed

One share class's seeded bucket values.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**share_class_short_code** | **str** | The short code of the seeded share class. | 
**buckets** | [**List[BucketSeedValue]**](BucketSeedValue.md) | The seeded buckets of the share class. | 
## Example

```python
from lusid.models.bucket_set_class_seed import BucketSetClassSeed
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

share_class_short_code: StrictStr = "example_share_class_short_code"
buckets: List[BucketSeedValue] = # Replace with your value
bucket_set_class_seed_instance = BucketSetClassSeed(share_class_short_code=share_class_short_code, buckets=buckets)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

