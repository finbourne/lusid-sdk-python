# BucketSeedValueRequest

One bucket's cumulative value to seed.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_id** | **str** | The identifier of the seeded bucket. | 
**absolute_value** | **float** | The bucket&#39;s cumulative value at the valuation point, in the fund currency. It is trusted input: nothing reconciles it to the share class NAV. | 
**per_unit_value** | **float** | The bucket&#39;s cumulative value per unit in issue. It is stored rounded to the share class&#39;s price precision. When omitted on a unitised bucket it is the absolute value over the share class&#39;s units in issue at the valuation point. Must be omitted on a bucket that is not unitised. | [optional] 
## Example

```python
from lusid.models.bucket_seed_value_request import BucketSeedValueRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

bucket_id: StrictStr = "example_bucket_id"
absolute_value: Union[StrictFloat, StrictInt] = # Replace with your value
per_unit_value: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
bucket_seed_value_request_instance = BucketSeedValueRequest(bucket_id=bucket_id, absolute_value=absolute_value, per_unit_value=per_unit_value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

