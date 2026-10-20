# DeleteWithholdingTaxRateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**series_identifiers** | **Dict[str, Optional[object]]** | The series identifiers that, with effectiveAt, identify the rate row: taxCountry, profileType and the dataset&#39;s own matching dimensions, structured according to its field schema. ruleSource is not accepted here: pass it as the ruleSource query parameter, which applies it to every row in the batch, and omit it for rows that apply at every source. | [optional] 
**effective_at** | **str** | The effectiveAt or cut-label datetime of the DataPoint. | 
## Example

```python
from lusid.models.delete_withholding_tax_rate_request import DeleteWithholdingTaxRateRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

series_identifiers: Optional[Dict[str, Any]] = # Replace with your value
effective_at: StrictStr = "example_effective_at"
delete_withholding_tax_rate_request_instance = DeleteWithholdingTaxRateRequest(series_identifiers=series_identifiers, effective_at=effective_at)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

