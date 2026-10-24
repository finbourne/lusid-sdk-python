# AllocationPostingFundLine

One transaction a booking writes on the fund's own books.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The deterministic identifier of the posting: the booking reference, investor record, commitment line, component and side. | [optional] 
**portfolio** | [**ResourceId**](ResourceId.md) |  | [optional] 
**transaction_type** | **str** | The transaction type the booking writes on the fund side, for instance PECall: the type the fund&#39;s configuration maps the partnership transaction type to. | [optional] 
**partnership_transaction_type** | **str** | The partnership transaction type the fund-side posting is classified as, for instance PA.ContributionCalled. | [optional] 
**amount** | **float** | The amount posted, in the event currency. | [optional] 
**component** | **str** | The component of the event the posting carries. | [optional] 
**investor_record_id** | **str** | The investor record the posting is for. | [optional] 
**via_vehicle** | **str** | The vehicle the investor&#39;s share reached the fund through, when it did not come direct. | [optional] 
**admission_vehicle** | **str** | The vehicle the investor was admitted to. | [optional] 
## Example

```python
from lusid.models.allocation_posting_fund_line import AllocationPostingFundLine
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: Optional[StrictStr] = "example_id"
portfolio: Optional[ResourceId] = None
transaction_type: Optional[StrictStr] = "example_transaction_type"
partnership_transaction_type: Optional[StrictStr] = "example_partnership_transaction_type"
amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
component: Optional[StrictStr] = "example_component"
investor_record_id: Optional[StrictStr] = "example_investor_record_id"
via_vehicle: Optional[StrictStr] = "example_via_vehicle"
admission_vehicle: Optional[StrictStr] = "example_admission_vehicle"
allocation_posting_fund_line_instance = AllocationPostingFundLine(id=id, portfolio=portfolio, transaction_type=transaction_type, partnership_transaction_type=partnership_transaction_type, amount=amount, component=component, investor_record_id=investor_record_id, via_vehicle=via_vehicle, admission_vehicle=admission_vehicle)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

