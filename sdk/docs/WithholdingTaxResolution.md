# WithholdingTaxResolution

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resolution_status** | **str** | Match or NoMatch: the status booking stamps on a transaction. | 
**matched_rule** | [**WithholdingTaxMatchedRule**](WithholdingTaxMatchedRule.md) |  | [optional] 
**rate_tiers** | [**WithholdingTaxRateTiers**](WithholdingTaxRateTiers.md) |  | [optional] 
**ras_flags** | [**WithholdingTaxReliefAtSourceFlags**](WithholdingTaxReliefAtSourceFlags.md) |  | [optional] 
**derived_split** | [**WithholdingTaxRateSplit**](WithholdingTaxRateSplit.md) |  | [optional] 
**provenance** | [**WithholdingTaxResolutionProvenance**](WithholdingTaxResolutionProvenance.md) |  | [optional] 
**resolved_dimensions** | **Dict[str, Optional[str]]** | Each dimension of either dataset, with the value used. Null where there is no value. | 
**is_what_if** | **bool** | False when the saved configuration&#39;s datasets and source order are used as they are. True when a dataset or the source order differs from the configuration&#39;s, or when no configuration was given. | 
**unresolved_dimensions** | [**Dict[str, WithholdingTaxUnresolvedDimension]**](WithholdingTaxUnresolvedDimension.md) | Each dimension that booking reads from the transaction, portfolio or fund, that dimensions does not supply, and that a couldAlsoMatch entry needs. It is null, so only rows blank on it match. Empty in Raw mode. | 
**could_also_match** | [**List[WithholdingTaxAlternativeMatch]**](WithholdingTaxAlternativeMatch.md) | Each other row that booking would choose with its own values for the unresolved dimensions, fewest values first, up to the limit. Where one entry&#39;s values include another&#39;s, the one with more values applies. | 
**has_more_alternatives** | **bool** | True when the limit stopped the lookup before it tried every combination of values, so couldAlsoMatch may miss rows. Ask again with a higher limit. | 
## Example

```python
from lusid.models.withholding_tax_resolution import WithholdingTaxResolution
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

resolution_status: StrictStr = "example_resolution_status"
matched_rule: Optional[WithholdingTaxMatchedRule] = # Replace with your value
rate_tiers: Optional[WithholdingTaxRateTiers] = # Replace with your value
ras_flags: Optional[WithholdingTaxReliefAtSourceFlags] = # Replace with your value
derived_split: Optional[WithholdingTaxRateSplit] = # Replace with your value
provenance: Optional[WithholdingTaxResolutionProvenance] = None
resolved_dimensions: Dict[str, Optional[StrictStr]] = # Replace with your value
is_what_if: StrictBool = # Replace with your value
is_what_if:StrictBool = True
unresolved_dimensions: Dict[str, WithholdingTaxUnresolvedDimension] = # Replace with your value
could_also_match: List[WithholdingTaxAlternativeMatch] = # Replace with your value
has_more_alternatives: StrictBool = # Replace with your value
has_more_alternatives:StrictBool = True
withholding_tax_resolution_instance = WithholdingTaxResolution(resolution_status=resolution_status, matched_rule=matched_rule, rate_tiers=rate_tiers, ras_flags=ras_flags, derived_split=derived_split, provenance=provenance, resolved_dimensions=resolved_dimensions, is_what_if=is_what_if, unresolved_dimensions=unresolved_dimensions, could_also_match=could_also_match, has_more_alternatives=has_more_alternatives)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

