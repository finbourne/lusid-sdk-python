# AllocationRule

The allocation character of one P&L or fees bucket of the allocation bucket set, and optionally how its pools  are shared, echoed as stored. The effective block, overridden fields and source are derived on the way out and  ignored on the way in, so a read written back pins nothing.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_id** | **str** | The bucket of the allocation bucket set the rule applies to. | 
**character** | **str** | The allocation character of the bucket&#39;s lines, which decides the capital account row. Available values: Income, RealisedGain, UnrealisedGain, OtherIncome, ManagementFee, Expense. Fixed by the set, and so omitted, when the allocation bucket set is a system set. | [optional] 
**basis** | **str** | The register balance the bucket&#39;s pools are shared on. Available values: CommittedCapital, PaidInCapital. Omit to take the character&#39;s default from allocationBases or the built-in default; returned as stored, with what the fund uses under effective. A pool that names its origin member is shared on deal paid-in unless its rule names a basis, and a rule may not ask for deal paid-in. Available values: CommittedCapital, PaidInCapital. | [optional] 
**exemption** | **str** | Which register flag sits a partner out of the bucket&#39;s pools. Available values: None, FeeExempt, ExpenseExempt. Omit to take the character&#39;s default (FeeExempt for ManagementFee, ExpenseExempt for Expense, otherwise None); returned as stored, with what the fund uses under effective. Available values: None, FeeExempt, ExpenseExempt. | [optional] 
**excluded_investor_record_ids** | **List[str]** | Investor records that sit out every pool of the bucket. Optional. | [optional] 
**effective** | [**AllocationRuleEffective**](AllocationRuleEffective.md) |  | [optional] 
**overridden_fields** | **List[str]** | On a system set&#39;s rule, the fields this configuration overrides; absent on a configuration&#39;s own rule. Read-only. | [optional] 
**source** | **str** | Where the rule&#39;s character comes from: System for a released system set, Configuration for the configuration&#39;s own set. Read-only. | [optional] 
## Example

```python
from lusid.models.allocation_rule import AllocationRule
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

bucket_id: StrictStr = "example_bucket_id"
character: Optional[StrictStr] = "example_character"
basis: Optional[StrictStr] = "example_basis"
exemption: Optional[StrictStr] = "example_exemption"
excluded_investor_record_ids: Optional[List[StrictStr]] = # Replace with your value
effective: Optional[AllocationRuleEffective] = None
overridden_fields: Optional[List[StrictStr]] = # Replace with your value
source: Optional[StrictStr] = "example_source"
allocation_rule_instance = AllocationRule(bucket_id=bucket_id, character=character, basis=basis, exemption=exemption, excluded_investor_record_ids=excluded_investor_record_ids, effective=effective, overridden_fields=overridden_fields, source=source)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

