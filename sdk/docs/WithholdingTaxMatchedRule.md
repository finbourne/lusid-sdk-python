# WithholdingTaxMatchedRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matched_rule_id** | **str** | The identifier booking stamps for the matched row: its series identifiers and effective date. | 
**matched_dataset** | **str** | The dataset the matched row came from: Main or Anomaly. | 
**rule_source** | **str** | The rule source of the matched row. Null when the row has none. | [optional] 
**effective_at** | **datetime** | The effective date of the matched row version. | 
## Example

```python
from lusid.models.withholding_tax_matched_rule import WithholdingTaxMatchedRule
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

matched_rule_id: StrictStr = "example_matched_rule_id"
matched_dataset: StrictStr = "example_matched_dataset"
rule_source: Optional[StrictStr] = "example_rule_source"
effective_at: datetime = # Replace with your value
withholding_tax_matched_rule_instance = WithholdingTaxMatchedRule(matched_rule_id=matched_rule_id, matched_dataset=matched_dataset, rule_source=rule_source, effective_at=effective_at)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

