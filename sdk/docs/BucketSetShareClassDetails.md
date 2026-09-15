# BucketSetShareClassDetails

Identifying detail for the share class a bucket set node is for.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lusid_instrument_id** | **str** | LUSID&#39;s internal unique instrument identifier for the share class&#39; instrument. Absent where the instrument has not been resolved. | [optional] 
**instrument_scope** | **str** | The scope in which the share class instrument lies. Absent where the instrument has not been resolved. | [optional] 
**short_code** | **str** | The unique code within the fund for the share class. | 
**dom_currency** | **str** | The domestic currency declared for the share class. | [optional] 
**instrument_active** | **bool** | Whether the share class&#39; instrument is active. | 
## Example

```python
from lusid.models.bucket_set_share_class_details import BucketSetShareClassDetails
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

lusid_instrument_id: Optional[StrictStr] = "example_lusid_instrument_id"
instrument_scope: Optional[StrictStr] = "example_instrument_scope"
short_code: StrictStr = "example_short_code"
dom_currency: Optional[StrictStr] = "example_dom_currency"
instrument_active: StrictBool = # Replace with your value
instrument_active:StrictBool = True
bucket_set_share_class_details_instance = BucketSetShareClassDetails(lusid_instrument_id=lusid_instrument_id, instrument_scope=instrument_scope, short_code=short_code, dom_currency=dom_currency, instrument_active=instrument_active)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

