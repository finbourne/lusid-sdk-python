# TranslationScriptId

Id of the Translation Script.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | Scope of the translation script. | 
**code** | **str** | Code of the translation script. | 
**version** | **str** | Semantic Version of the translation script of the form MAJOR.MINOR.PATCH. | 
## Example

```python
from lusid.models.translation_script_id import TranslationScriptId
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

scope: StrictStr = "example_scope"
code: StrictStr = "example_code"
version: StrictStr = "example_version"
translation_script_id_instance = TranslationScriptId(scope=scope, code=code, version=version)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

