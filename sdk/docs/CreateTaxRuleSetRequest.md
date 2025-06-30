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
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr, validator

id: ResourceId = # Replace with your value
display_name: StrictStr = "example_display_name"
description: StrictStr = "example_description"
output_property_key: StrictStr = "example_output_property_key"
rules: conlist(TaxRule, max_items=100) = Field(...)
create_tax_rule_set_request_instance = CreateTaxRuleSetRequest(id=id, display_name=display_name, description=description, output_property_key=output_property_key, rules=rules)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

