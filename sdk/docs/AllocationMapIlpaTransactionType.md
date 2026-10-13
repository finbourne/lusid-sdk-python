# AllocationMapIlpaTransactionType

The ILPA transaction type an Allocation Map reports one kind of allocation event under, overriding the default.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** | The kind of allocation event the ILPA transaction type applies to: CapitalCall, Distribution, FeeExpense, ValuationMove, Equalisation, RecallExpiry, Transfer, Default or Commitment. Available values: CapitalCall, Distribution, FeeExpense, ValuationMove, Commitment, Equalisation, RecallExpiry, Transfer, Default, DealFunding. | 
**ilpa_transaction_type** | **str** | The ILPA transaction type events of this kind are reported under, for example &#39;Capital Call: Investments&#39; or &#39;Distribution: Recallable&#39;. Must be a value of the system IlpaTransactionType data type. | 
**component** | **str** | The component of the event the ILPA transaction type applies to, for example MgmtFee or ROC. Absent means the entry is the default for every component of the event type without an entry of its own. | [optional] 
## Example

```python
from lusid.models.allocation_map_ilpa_transaction_type import AllocationMapIlpaTransactionType
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

event_type: StrictStr = "example_event_type"
ilpa_transaction_type: StrictStr = "example_ilpa_transaction_type"
component: Optional[StrictStr] = "example_component"
allocation_map_ilpa_transaction_type_instance = AllocationMapIlpaTransactionType(event_type=event_type, ilpa_transaction_type=ilpa_transaction_type, component=component)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

