# ManagementFeeResplitRequest

The request to re-split a partnership fund's prepaid management fee periods between the fee payable and the  receivable from the manager.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_start** | **datetime** | The start of the window to re-split, exclusive: every prepaid period whose window meets it is re-split. Defaults to the fund&#39;s earliest prepaid period. | [optional] 
**period_end** | **datetime** | The end of the window to re-split, inclusive. Defaults to the latest prepaid period. | [optional] 
**dry_run** | **bool** | When true, nothing is written and the response says which prepaid periods&#39; splits are out of date. Defaults to false. | [optional] 
## Example

```python
from lusid.models.management_fee_resplit_request import ManagementFeeResplitRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

period_start: Optional[datetime] = # Replace with your value
period_end: Optional[datetime] = # Replace with your value
dry_run: Optional[StrictBool] = # Replace with your value
dry_run:Optional[StrictBool] = None
management_fee_resplit_request_instance = ManagementFeeResplitRequest(period_start=period_start, period_end=period_end, dry_run=dry_run)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

