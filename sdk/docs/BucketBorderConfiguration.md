# BucketBorderConfiguration

Configuration determining how the borders of bucket intervals behave when allocating cash flows to buckets.  When supplied, cash flows are bucketed into intervals defined by the bucketing dates rather than being  rounded to the nearest bucketing date.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_inclusive** | **bool** | Is the start of the first bucket interval inclusive of its start date. Defaults to true. | [optional] 
**end_inclusive** | **bool** | Is the end of the last bucket interval inclusive of its end date. Defaults to false. | [optional] 
**boundary_belongs_to** | **str** | For boundaries shared by two adjacent intervals, which interval a cash flow falling exactly on the  boundary belongs to. Supported string (enumeration) values are: [Earlier, Later]. Defaults to &#39;Earlier&#39;. Available values: Earlier, Later. | [optional] 
## Example

```python
from lusid.models.bucket_border_configuration import BucketBorderConfiguration
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

start_inclusive: Optional[StrictBool] = # Replace with your value
start_inclusive:Optional[StrictBool] = None
end_inclusive: Optional[StrictBool] = # Replace with your value
end_inclusive:Optional[StrictBool] = None
boundary_belongs_to: Optional[StrictStr] = "example_boundary_belongs_to"
bucket_border_configuration_instance = BucketBorderConfiguration(start_inclusive=start_inclusive, end_inclusive=end_inclusive, boundary_belongs_to=boundary_belongs_to)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

