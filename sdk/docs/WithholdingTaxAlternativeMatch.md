# WithholdingTaxAlternativeMatch

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**if_values** | **Dict[str, Optional[str]]** | The values of the unresolved dimensions that choose this row, one or more. | 
**matched_rule_id** | **str** | The identifier booking would stamp for the row that these values choose. | 
**stop_at_source_rate** | **float** | The rate that this row would withhold at source. | 
## Example

```python
from lusid.models.withholding_tax_alternative_match import WithholdingTaxAlternativeMatch
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

if_values: Dict[str, Optional[StrictStr]] = # Replace with your value
matched_rule_id: StrictStr = "example_matched_rule_id"
stop_at_source_rate: Union[StrictFloat, StrictInt] = # Replace with your value
withholding_tax_alternative_match_instance = WithholdingTaxAlternativeMatch(if_values=if_values, matched_rule_id=matched_rule_id, stop_at_source_rate=stop_at_source_rate)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

