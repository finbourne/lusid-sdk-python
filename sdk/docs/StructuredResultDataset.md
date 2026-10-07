# StructuredResultDataset

Contains the run-time parameters that are appropriate for check definitions  with datasetSchema.type = \"StructuredResultData\". Names one structured result data document.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_at** | **datetime** | The effectiveAt date of the document&#39;s rows to check. Required. | [optional] 
**as_at** | **datetime** | The asAt date to fetch the data. Nullable. Defaults to latest. | [optional] 
**scope** | **str** | The scope of the document. Required. | [optional] 
**code** | **str** | The code of the document. Required. | [optional] 
**source** | **str** | The platform or vendor that provided the document, e.g. \&quot;Client\&quot;. Required. | [optional] 
**result_type** | **str** | The document&#39;s result type, e.g. \&quot;UnitResult/Custom\&quot;. Required. | [optional] 
**row_selector_attribute** | **str** | A row field to narrow down the rows checked, e.g. rowId[&#39;Instrument/default/LusidInstrumentId&#39;] or  rowData[&#39;Valuation/PV&#39;].Units. Cannot be provided without rowSelectorValue, and vice versa. | [optional] 
**row_selector_value** | **str** | The value of the above row field used to narrow down the rows. Cannot be provided without  rowSelectorAttribute, and vice versa. | [optional] 
## Example

```python
from lusid.models.structured_result_dataset import StructuredResultDataset
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

effective_at: Optional[datetime] = # Replace with your value
as_at: Optional[datetime] = # Replace with your value
scope: Optional[StrictStr] = "example_scope"
code: Optional[StrictStr] = "example_code"
source: Optional[StrictStr] = "example_source"
result_type: Optional[StrictStr] = "example_result_type"
row_selector_attribute: Optional[StrictStr] = "example_row_selector_attribute"
row_selector_value: Optional[StrictStr] = "example_row_selector_value"
structured_result_dataset_instance = StructuredResultDataset(effective_at=effective_at, as_at=as_at, scope=scope, code=code, source=source, result_type=result_type, row_selector_attribute=row_selector_attribute, row_selector_value=row_selector_value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

