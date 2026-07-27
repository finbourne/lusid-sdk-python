# TypedResourceId

Represents the user-defined identifier for a Legal Entity.  Users can define their own, scoped identifiers for Legal Entities using identifier properties.  For example,  when used to identify a Legal Entity, the identifier defined by LegalEntity/myScope/1234ABC0000000000063 would be represented as   {     \"idTypeScope\": \"myScope\",     \"idTypeCode\": \"1234ABC0000000000063\",     \"code\": \"ACME_CO\"   }
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_type_scope** | **str** | The scope of the identifier&#39;s (property) definition. | 
**id_type_code** | **str** | The code of identifier&#39;s (property) definition. This describes what the identifier represents.  For a Legal Entity, this might be a registeredCompanyNumber or LEI. | 
**code** | **str** | The value of the user-defined identifier in respect of the entity. | 
## Example

```python
from lusid.models.typed_resource_id import TypedResourceId
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id_type_scope: StrictStr = "example_id_type_scope"
id_type_code: StrictStr = "example_id_type_code"
code: StrictStr = "example_code"
typed_resource_id_instance = TypedResourceId(id_type_scope=id_type_scope, id_type_code=id_type_code, code=code)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

