# FileResponse

Allows a file (represented as a stream) to be returned from an Api call
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_stream** | **bytearray** |  | [optional] 
**content_type** | **str** |  | [optional] 
**downloaded_filename** | **str** |  | [optional] 
## Example

```python
from lusid.models.file_response import FileResponse
from typing import Any, Dict, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictBytes, StrictStr

file_stream: Optional[Union[StrictBytes, StrictStr]] = # Replace with your value
content_type: Optional[StrictStr] = "example_content_type"
downloaded_filename: Optional[StrictStr] = "example_downloaded_filename"
file_response_instance = FileResponse(file_stream=file_stream, content_type=content_type, downloaded_filename=downloaded_filename)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

