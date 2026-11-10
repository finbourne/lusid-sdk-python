# UpsertTaxCostRecordsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successes** | [**Dict[str, TaxCostRecord]**](TaxCostRecord.md) | The Tax Cost Records that were successfully upserted, keyed by the code supplied in the request. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The Tax Cost Records that failed to upsert, keyed by the code supplied in the request, with the reason for each failure. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.upsert_tax_cost_records_response import UpsertTaxCostRecordsResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

successes: Optional[Dict[str, TaxCostRecord]] = # Replace with your value
failed: Optional[Dict[str, ErrorDetail]] = # Replace with your value
links: Optional[List[Link]] = None
upsert_tax_cost_records_response_instance = UpsertTaxCostRecordsResponse(successes=successes, failed=failed, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

