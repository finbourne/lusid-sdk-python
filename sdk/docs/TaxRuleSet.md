# TaxRuleSet

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | A user-friendly name | 
**description** | **str** | A description of what this rule set is for | 
**output_property_key** | **str** | The property key that this rule set will write to | 
**rules** | [**List[TaxRule]**](TaxRule.md) | The rules of this rule set, which stipulate what rate to apply (i.e. write to the OutputPropertyKey) under certain conditions | 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.tax_rule_set import TaxRuleSet
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: ResourceId
display_name: StrictStr = "example_display_name"
description: StrictStr = "example_description"
output_property_key: StrictStr = "example_output_property_key"
rules: List[TaxRule] = # Replace with your value
version: Optional[Version] = None
links: Optional[List[Link]] = None
tax_rule_set_instance = TaxRuleSet(id=id, display_name=display_name, description=description, output_property_key=output_property_key, rules=rules, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

