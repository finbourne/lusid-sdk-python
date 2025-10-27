# CreateTaxRuleSetRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** |  | 
**description** | **str** |  | 
**output_property_key** | **str** |  | 
**rules** | [**List[TaxRule]**](TaxRule.md) |  | 
## Example

```python
from lusid.models.create_tax_rule_set_request import CreateTaxRuleSetRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: ResourceId
display_name: StrictStr = "example_display_name"
description: StrictStr = "example_description"
output_property_key: StrictStr = "example_output_property_key"
rules: List[TaxRule]
create_tax_rule_set_request_instance = CreateTaxRuleSetRequest(id=id, display_name=display_name, description=description, output_property_key=output_property_key, rules=rules)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

