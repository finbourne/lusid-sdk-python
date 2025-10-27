# VirtualDocumentRow

Rows identified by the composite id, based on the data maps
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**row_id** | **Dict[str, Optional[str]]** | The identifier for the row. This is keyed by address keys, and values obtained through applying the data map to the documents. | [optional] 
**row_data** | [**GroupedResultOfAddressKey**](GroupedResultOfAddressKey.md) |  | [optional] 
## Example

```python
from lusid.models.virtual_document_row import VirtualDocumentRow
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

row_id: Optional[Dict[str, Optional[StrictStr]]] = # Replace with your value
row_data: Optional[GroupedResultOfAddressKey] = # Replace with your value
virtual_document_row_instance = VirtualDocumentRow(row_id=row_id, row_data=row_data)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

