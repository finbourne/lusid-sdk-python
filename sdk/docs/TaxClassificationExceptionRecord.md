# TaxClassificationExceptionRecord

An instrument the engine could not classify, or a qualifying-investments flip, for the exceptions feed.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**luid** | **str** | The LUSID instrument identifier of the instrument the exception was raised for. | 
**instrument_name** | **str** | The name of the instrument the exception was raised for. | [optional] 
**exception** | [**TaxClassificationException**](TaxClassificationException.md) |  | 
**effective_at** | **datetime** | The effective date the exception was observed at. | 
**as_at** | **datetime** | The asAt time the exception was observed at. | 
## Example

```python
from lusid.models.tax_classification_exception_record import TaxClassificationExceptionRecord
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

luid: StrictStr = "example_luid"
instrument_name: Optional[StrictStr] = "example_instrument_name"
exception: TaxClassificationException
effective_at: datetime = # Replace with your value
as_at: datetime = # Replace with your value
tax_classification_exception_record_instance = TaxClassificationExceptionRecord(luid=luid, instrument_name=instrument_name, exception=exception, effective_at=effective_at, as_at=as_at)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

