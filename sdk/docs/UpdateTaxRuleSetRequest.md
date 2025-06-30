# UpdateTaxRuleSetRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | 
**description** | **str** |  | 
**rules** | [**List[TaxRule]**](TaxRule.md) |  | 
## Example

```python
from lusid.models.update_tax_rule_set_request import UpdateTaxRuleSetRequest
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, conlist, constr, validator

display_name: StrictStr = "example_display_name"
description: StrictStr = "example_description"
rules: conlist(TaxRule, max_items=100) = Field(...)
update_tax_rule_set_request_instance = UpdateTaxRuleSetRequest(display_name=display_name, description=description, rules=rules)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

