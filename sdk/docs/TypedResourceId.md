# TypedResourceId

Represents the user-defined identifier for a Legal Entity or Person.  Users can define their own, scoped identifiers for Legal Entities and Persons using identifier properties.  For example,  when used to identify a Person, the identifier defined by Person/myScope/username would be represented as   {     \"idTypeScope\": \"myScope\",     \"idTypeCode\": \"username\",     \"code\": \"john_doe_001\"   }
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_type_scope** | **str** | The scope of the identifier&#39;s (property) definition. | 
**id_type_code** | **str** | The code of identifier&#39;s (property) definition. This describes what the identifier represents.  For a Person this might be a username, nationalInsuranceNumber or similar.  For a Legal Entity, this might be a registeredCompanyNumber or LEI. | 
**code** | **str** | The value of the user-defined identifier in respect of the entity. | 
## Example

```python
from lusid.models.typed_resource_id import TypedResourceId
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr, validator

id_type_scope: StrictStr = "example_id_type_scope"
id_type_code: StrictStr = "example_id_type_code"
code: StrictStr = "example_code"
typed_resource_id_instance = TypedResourceId(id_type_scope=id_type_scope, id_type_code=id_type_code, code=code)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

