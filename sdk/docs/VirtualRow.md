# VirtualRow

Rows identified by the composite id, based on the data maps
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**row_id** | **Dict[str, str]** | The identifier for the row. This is keyed by address keys, and values obtained through applying the data map to the documents. | [optional] 
**row_data** | [**Dict[str, ResultValue]**](ResultValue.md) | The data for the particular row | [optional] 
## Example

```python
from lusid.models.virtual_row import VirtualRow
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr

row_id: Optional[Dict[str, StrictStr]] = # Replace with your value
row_data: Optional[Dict[str, ResultValue]] = # Replace with your value
virtual_row_instance = VirtualRow(row_id=row_id, row_data=row_data)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

