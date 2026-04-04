# SeriesDefinitionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**share_class_code** | **str** | The code of the Share Class this Series belongs to. | 
**series_definitions** | [**List[SeriesDefinition]**](SeriesDefinition.md) | The definitions of the Series to add to the Share Class. | 
## Example

```python
from lusid.models.series_definition_request import SeriesDefinitionRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

share_class_code: StrictStr = "example_share_class_code"
series_definitions: List[SeriesDefinition] = # Replace with your value
series_definition_request_instance = SeriesDefinitionRequest(share_class_code=share_class_code, series_definitions=series_definitions)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

