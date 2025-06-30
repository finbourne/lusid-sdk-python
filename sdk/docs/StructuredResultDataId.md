# StructuredResultDataId

An identifier that uniquely describes an item of structured result data such as the risk to an interest curve or a set of yields or analytics on an index.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | The platform or vendor that provided the structured result data, e.g. &#39;client&#39;. This is primarily of interest when data could have been sourced from multiple sources | 
**code** | **str** | The identifier for the entity that this id describes. It could be an index, instrument or other form of structured data | [optional] 
**effective_at** | **str** | The effectiveAt or cut label that this item of structured result data is/was updated/inserted with. | [optional] 
**result_type** | **str** | An identifier that denotes the class of data that the id points to. This is not the same as the format, but a more generic identifier such as &#39;risk result&#39;, &#39;cashflow&#39;, &#39;index&#39; or similar. | [optional] 
## Example

```python
from lusid.models.structured_result_data_id import StructuredResultDataId
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, constr, validator

source: StrictStr = "example_source"
code: Optional[StrictStr] = "example_code"
effective_at: Optional[StrictStr] = "example_effective_at"
result_type: Optional[StrictStr] = "example_result_type"
structured_result_data_id_instance = StructuredResultDataId(source=source, code=code, effective_at=effective_at, result_type=result_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

