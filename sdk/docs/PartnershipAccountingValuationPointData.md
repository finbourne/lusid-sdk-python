# PartnershipAccountingValuationPointData

The partnership accounting view of a valuation point: what is left on the income summary to allocate to the  partners, the configuration pack the allocation books under and, when the period cannot be allocated as it  stands, why.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unallocated_income_summary** | **float** | The profit and loss of the valuation point&#39;s period that has not yet been allocated to the partners: what the period&#39;s profit and loss lines, as the allocation bucket set classifies them, would pool, less what the partner allocation has posted for the period. Lines no bucket claims count as unallocated. Must be zero before the valuation point can be finalised. | 
**config_pack_scope** | **str** | The scope of the configuration pack. | 
**config_pack_code** | **str** | The code of the configuration pack. | 
**allocation_problem** | [**PartnershipAllocationProblem**](PartnershipAllocationProblem.md) |  | [optional] 
## Example

```python
from lusid.models.partnership_accounting_valuation_point_data import PartnershipAccountingValuationPointData
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

unallocated_income_summary: Union[StrictFloat, StrictInt] = # Replace with your value
config_pack_scope: StrictStr = "example_config_pack_scope"
config_pack_code: StrictStr = "example_config_pack_code"
allocation_problem: Optional[PartnershipAllocationProblem] = # Replace with your value
partnership_accounting_valuation_point_data_instance = PartnershipAccountingValuationPointData(unallocated_income_summary=unallocated_income_summary, config_pack_scope=config_pack_scope, config_pack_code=config_pack_code, allocation_problem=allocation_problem)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

