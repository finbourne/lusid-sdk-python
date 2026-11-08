# TaxExceptionItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | An identifier stable within a response, built from the category, portfolio and instrument. | 
**category** | **str** | The kind of exception: UnmatchedDisposal, NegativePool, MissingValuation or UnclassifiedInstrument. | 
**severity** | **str** | Error when the exception blocks the tax computation, Warning when it casts doubt on it. | 
**portfolio** | [**ResourceId**](ResourceId.md) |  | 
**instrument** | **str** | The LUSID unique identifier of the instrument the exception was raised against. | [optional] 
**message** | **str** | A description of the exception. | 
**raised_at** | **datetime** | The asAt the exception was observed at. | 
**tax_at_stake** | **float** | The tax effect, in the Fund&#39;s base currency, of the position or gain the exception blocks, at the Fund&#39;s configured rate. Absent when the rate or the exposure is not known. | [optional] 
**root_cause** | [**TaxExceptionRootCause**](TaxExceptionRootCause.md) |  | [optional] 
## Example

```python
from lusid.models.tax_exception_item import TaxExceptionItem
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: StrictStr = "example_id"
category: StrictStr = "example_category"
severity: StrictStr = "example_severity"
portfolio: ResourceId
instrument: Optional[StrictStr] = "example_instrument"
message: StrictStr = "example_message"
raised_at: datetime = # Replace with your value
tax_at_stake: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
root_cause: Optional[TaxExceptionRootCause] = # Replace with your value
tax_exception_item_instance = TaxExceptionItem(id=id, category=category, severity=severity, portfolio=portfolio, instrument=instrument, message=message, raised_at=raised_at, tax_at_stake=tax_at_stake, root_cause=root_cause)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

