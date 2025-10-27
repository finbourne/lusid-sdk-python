# Mapping

Defines the rule set to be used to determine if entries should be considered as a match.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The scope for this mapping. | 
**code** | **str** | The code for this mapping. | 
**name** | **str** | The mapping name | 
**reconciliation_type** | **str** | What type of reconciliation this mapping is for | 
**rules** | [**List[MappingRule]**](MappingRule.md) | The rules in this mapping, keyed by the left field/property name | [optional] 
## Example

```python
from lusid.models.mapping import Mapping
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

scope: StrictStr = "example_scope"
code: StrictStr = "example_code"
name: StrictStr = "example_name"
reconciliation_type: StrictStr = "example_reconciliation_type"
rules: Optional[List[MappingRule]] = # Replace with your value
mapping_instance = Mapping(scope=scope, code=code, name=name, reconciliation_type=reconciliation_type, rules=rules)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

