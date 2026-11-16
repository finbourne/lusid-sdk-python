# AllocationRuleEffective

What a rule's pools actually use once the defaults are applied. Read-only: derived on the way out and ignored on  the way in.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basis** | **str** | The basis the bucket&#39;s fund-level pools are shared on. Available values: CommittedCapital, PaidInCapital. | 
**exemption** | **str** | The register flag that sits partners out of the bucket&#39;s pools. Available values: None, FeeExempt, ExpenseExempt. | 
**report_row** | **str** | The capital account row the bucket&#39;s allocations land on, derived from the character. Available values: NetOperatingIncome, ManagementFeesGross, RealisedGainLoss, UnrealisedGainLoss. | [optional] 
**basis_level** | **str** | Which level of the basis precedence decided the basis. Available values: Rule, CharacterDefault, BuiltIn. | 
## Example

```python
from lusid.models.allocation_rule_effective import AllocationRuleEffective
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

basis: StrictStr = "example_basis"
exemption: StrictStr = "example_exemption"
report_row: Optional[StrictStr] = "example_report_row"
basis_level: StrictStr = "example_basis_level"
allocation_rule_effective_instance = AllocationRuleEffective(basis=basis, exemption=exemption, report_row=report_row, basis_level=basis_level)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

