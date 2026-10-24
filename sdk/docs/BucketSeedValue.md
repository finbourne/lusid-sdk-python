# BucketSeedValue

One bucket's seeded cumulative value, as stored.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_id** | **str** | The identifier of the seeded bucket. | 
**absolute_value** | **float** | The bucket&#39;s seeded cumulative value at the valuation point, in the fund currency. | 
**per_unit_value** | **float** | The per-unit value given with the seed, unrounded. Omitted where none was given, in which case the valuation point reads it off the share class&#39;s units in issue. | [optional] 
## Example

```python
from lusid.models.bucket_seed_value import BucketSeedValue
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

bucket_id: StrictStr = "example_bucket_id"
absolute_value: Union[StrictFloat, StrictInt] = # Replace with your value
per_unit_value: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
bucket_seed_value_instance = BucketSeedValue(bucket_id=bucket_id, absolute_value=absolute_value, per_unit_value=per_unit_value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

