# AmortisationRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the rule. | 
**description** | **str** | A description of the rule. | [optional] 
**filter** | **str** | The filter for this rule. | 
**amortisation_method** | **str** | The filter for this rule. | 
## Example

```python
from lusid.models.amortisation_rule import AmortisationRule
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr, validator

name: StrictStr = "example_name"
description: Optional[StrictStr] = "example_description"
filter: StrictStr = "example_filter"
amortisation_method: StrictStr = "example_amortisation_method"
amortisation_rule_instance = AmortisationRule(name=name, description=description, filter=filter, amortisation_method=amortisation_method)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

