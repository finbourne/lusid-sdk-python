# TaxRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A user-friendly name | 
**description** | **str** | A description for this rule | 
**rate** | **float** | The rate to be applied if all criteria are met | 
**match_criteria** | [**List[MatchCriterion]**](MatchCriterion.md) | A set of criteria to be met for this rule to be applied | 
## Example

```python
from lusid.models.tax_rule import TaxRule
from typing import Any, Dict, List, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, conlist, constr, validator

name: StrictStr = "example_name"
description: StrictStr = "example_description"
rate: Union[StrictFloat, StrictInt] = # Replace with your value
match_criteria: conlist(MatchCriterion, max_items=20) = Field(..., alias="matchCriteria", description="A set of criteria to be met for this rule to be applied")
tax_rule_instance = TaxRule(name=name, description=description, rate=rate, match_criteria=match_criteria)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

