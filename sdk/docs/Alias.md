# Alias

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_name** | **str** | The property key, identifier type, or field to be replaced by an alias. | 
**attribute_alias** | **str** | The alias to replace the property key, identifier type, or field on the bound entity. | 
## Example

```python
from lusid.models.alias import Alias
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr, validator

attribute_name: StrictStr = "example_attribute_name"
attribute_alias: StrictStr = "example_attribute_alias"
alias_instance = Alias(attribute_name=attribute_name, attribute_alias=attribute_alias)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

