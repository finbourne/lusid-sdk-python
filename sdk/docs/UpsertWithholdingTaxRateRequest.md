# UpsertWithholdingTaxRateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**series_identifiers** | **Dict[str, Optional[object]]** | The identifiers that uniquely define this DataSeries, if any, structured according to the FieldSchema of the parent RelationalDatasetDefinition. | [optional] 
**effective_at** | **str** | The effectiveAt or cut-label datetime of the DataPoint. | 
**value_fields** | **Dict[str, Optional[object]]** | The values associated with the DataPoint, structured according to the FieldSchema of the parent RelationalDatasetDefinition. | 
**meta_data_fields** | **Dict[str, Optional[object]]** | The metadata associated with the DataPoint, structured according to the FieldSchema of the parent RelationalDatasetDefinition. | [optional] 
## Example

```python
from lusid.models.upsert_withholding_tax_rate_request import UpsertWithholdingTaxRateRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

series_identifiers: Optional[Dict[str, Any]] = # Replace with your value
effective_at: StrictStr = "example_effective_at"
value_fields: Dict[str, Any] = # Replace with your value
meta_data_fields: Optional[Dict[str, Any]] = # Replace with your value
upsert_withholding_tax_rate_request_instance = UpsertWithholdingTaxRateRequest(series_identifiers=series_identifiers, effective_at=effective_at, value_fields=value_fields, meta_data_fields=meta_data_fields)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

