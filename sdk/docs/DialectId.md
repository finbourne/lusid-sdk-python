# DialectId

Unique identifier of a given Dialect
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The Scope of the dialect. | 
**vendor** | **str** | The vendor of the dialect, the entity that created it. e.g. ISDA, FINBOURNE. | 
**source_system** | **str** | The source system of the dialect, the system that understands it. e.g. LUSID, QuantLib. | 
**version** | **str** | The semantic version of the dialect: MAJOR.MINOR.PATCH. | 
**serialisation_format** | **str** | The serialisation format of a document in this dialect. e.g. JSON, XML. | 
**entity_type** | **str** | The type of entity this dialect describes e.g. Instrument. | 
## Example

```python
from lusid.models.dialect_id import DialectId
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr, validator

scope: StrictStr = "example_scope"
vendor: StrictStr = "example_vendor"
source_system: StrictStr = "example_source_system"
version: StrictStr = "example_version"
serialisation_format: StrictStr = "example_serialisation_format"
entity_type: StrictStr = "example_entity_type"
dialect_id_instance = DialectId(scope=scope, vendor=vendor, source_system=source_system, version=version, serialisation_format=serialisation_format, entity_type=entity_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

