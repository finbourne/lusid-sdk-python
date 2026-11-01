# DealingEstimates

How a fund treats estimated dealing when it strikes a valuation point before dealing is final.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sources** | **List[str]** | Where the Fund&#39;s dealing estimates are read from: LusidTA, orders held in LUSID Transfer Agency, or External, orders dealt outside LUSID and reported to it. At least one, each at most once. Naming both sums the two books with no de-duplication between them; each source&#39;s completeness is tracked on its own. Available values: LusidTA, External. | 
**require_complete** | **bool** | Whether the dealing book must be complete before a swing is proposed. For the LusidTA source the book is complete once each share class&#39;s TA/DealingSchedule cut-off has passed at the strike&#39;s as-at; a class with no cut-off configured is treated as complete and the audit says so. An order written after its class&#39;s cut-off is late: reported on the audit but not counted. When true and the book is incomplete the valuation point is still struck, at the unswung baseline, and no swing is proposed; the audit says why. Defaults to true. | [optional] 
**count_pending** | **bool** | Whether a Pending order at the valuation point counts towards the estimated flow. Orders in the New and Priced states always count. When true a Pending order is folded into the flows like them; when false it is left out of the decision and reported on the audit as pending and not counted, with its value where one can be read. Defaults to false. | [optional] 
**unit_valuation** | **str** | The price estimated flows are turned into units at: EstimatePrice, the estimate struck at this valuation point, or LastOfficialPrice, the last official dealing price the Fund published. Available values: EstimatePrice, LastOfficialPrice. | 
## Example

```python
from lusid.models.dealing_estimates import DealingEstimates
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

sources: List[StrictStr] = # Replace with your value
require_complete: Optional[StrictBool] = # Replace with your value
require_complete:Optional[StrictBool] = None
count_pending: Optional[StrictBool] = # Replace with your value
count_pending:Optional[StrictBool] = None
unit_valuation: StrictStr = "example_unit_valuation"
dealing_estimates_instance = DealingEstimates(sources=sources, require_complete=require_complete, count_pending=count_pending, unit_valuation=unit_valuation)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

