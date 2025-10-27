# StructuredResultData

An item of structured result data that is to be inserted into Lusid. This will typically be a Json or Xml document that  contains a set of result data appropriate to a specific entity such as an instrument or potentially an index.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_format** | **str** | The format of the accompanying document. | 
**version** | **str** | The semantic version of the document format; MAJOR.MINOR.PATCH | [optional] 
**name** | **str** | The name or description for the document | [optional] 
**document** | **str** | The document that will be stored (or retrieved) and which describes a unit result data entity such as a set of prices or yields | 
**data_map_key** | [**DataMapKey**](DataMapKey.md) |  | [optional] 
## Example

```python
from lusid.models.structured_result_data import StructuredResultData
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

document_format: StrictStr = "example_document_format"
version: Optional[StrictStr] = "example_version"
name: Optional[StrictStr] = "example_name"
document: StrictStr = "example_document"
data_map_key: Optional[DataMapKey] = # Replace with your value
structured_result_data_instance = StructuredResultData(document_format=document_format, version=version, name=name, document=document, data_map_key=data_map_key)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

