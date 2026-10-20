# WithholdingTaxResolutionProvenance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_score** | **float** | The share of the main dataset&#39;s dimensions that the row matches, from 0 to 1. Null on an anomaly match. | [optional] 
**matched_field_count** | **int** | The number of the main dataset&#39;s dimensions that the row matches. Null on an anomaly match. | [optional] 
**source_filter_applied** | **str** | The rule source level that matched. Null when no source priority applies. | [optional] 
**tie_broken** | **bool** | True when another row matched as well as the winner, so the tie-break order chose: the latest effective date, then the rule id. | 
## Example

```python
from lusid.models.withholding_tax_resolution_provenance import WithholdingTaxResolutionProvenance
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

match_score: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
matched_field_count: Optional[StrictInt] = # Replace with your value
matched_field_count: Optional[StrictInt] = None
source_filter_applied: Optional[StrictStr] = "example_source_filter_applied"
tie_broken: StrictBool = # Replace with your value
tie_broken:StrictBool = True
withholding_tax_resolution_provenance_instance = WithholdingTaxResolutionProvenance(match_score=match_score, matched_field_count=matched_field_count, source_filter_applied=source_filter_applied, tie_broken=tie_broken)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

