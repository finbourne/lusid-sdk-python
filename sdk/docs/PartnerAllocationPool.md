# PartnerAllocationPool

One pool of an allocation run: an amount of a given character, split across the partners on a basis.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**character** | **str** | The character of the pool&#39;s amount, for example Income, RealisedGain or Expense. | 
**origin_member_short_code** | **str** | For a deal-linked pool, the short code of the member fund the amount originates from. | [optional] 
**pool_amount** | **float** | The amount in the pool. | 
**basis** | **str** | The basis the pool was shared on. Available values: CommittedCapital, PaidInCapital, DealPaidIn. | 
**basis_source** | **str** | Where the figures a deal pool was shared on came from; absent on a fund-level pool, which is shared on the register&#39;s balances. Available values: DealContributions (what each partner paid into the pool&#39;s deal, from the booked allocation events), Fallback (a deal pool no partner has paid into, shared on its character&#39;s fund-level basis instead). | [optional] 
**allocations** | [**List[PartnerAllocation]**](PartnerAllocation.md) | Each partner&#39;s share of the pool. | 
**residual** | **float** | The rounding residual, carried by the largest allocation. | 
**pool_id** | **str** | The pool&#39;s identifier: the allocation rule&#39;s bucket id, or TAG: followed by the character for lines pooled by their distribution character tag. | 
**bucket_set** | **str** | The code of the allocation bucket set the pool was classified by, with its version, for example PA-ALLOCATION-v1. | 
**basis_level** | **str** | Which level of the basis precedence decided the pool&#39;s basis. Available values: Rule (the bucket rule&#39;s own basis), CharacterDefault (the configuration&#39;s allocationBases entry for the character), BuiltIn (the built-in default for the character). | 
**exemption** | **str** | The register flag that sat partners out of the pool. Available values: None, FeeExempt, ExpenseExempt. | 
**excluded_investor_record_ids** | **List[str]** | The partners the pool&#39;s rule left out of it. | [optional] 
**report_row** | **str** | The capital account row the pool&#39;s allocations land on, derived from the character. Available values: NetOperatingIncome, ManagementFeesGross, RealisedGainLoss, UnrealisedGainLoss. | [optional] 
**sources** | [**PartnerAllocationPoolSources**](PartnerAllocationPoolSources.md) |  | 
## Example

```python
from lusid.models.partner_allocation_pool import PartnerAllocationPool
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

character: StrictStr = "example_character"
origin_member_short_code: Optional[StrictStr] = "example_origin_member_short_code"
pool_amount: Union[StrictFloat, StrictInt] = # Replace with your value
basis: StrictStr = "example_basis"
basis_source: Optional[StrictStr] = "example_basis_source"
allocations: List[PartnerAllocation] = # Replace with your value
residual: Union[StrictFloat, StrictInt] = # Replace with your value
pool_id: StrictStr = "example_pool_id"
bucket_set: StrictStr = "example_bucket_set"
basis_level: StrictStr = "example_basis_level"
exemption: StrictStr = "example_exemption"
excluded_investor_record_ids: Optional[List[StrictStr]] = # Replace with your value
report_row: Optional[StrictStr] = "example_report_row"
sources: PartnerAllocationPoolSources
partner_allocation_pool_instance = PartnerAllocationPool(character=character, origin_member_short_code=origin_member_short_code, pool_amount=pool_amount, basis=basis, basis_source=basis_source, allocations=allocations, residual=residual, pool_id=pool_id, bucket_set=bucket_set, basis_level=basis_level, exemption=exemption, excluded_investor_record_ids=excluded_investor_record_ids, report_row=report_row, sources=sources)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

