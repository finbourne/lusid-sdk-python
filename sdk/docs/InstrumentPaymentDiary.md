# InstrumentPaymentDiary

A payment diary containing all the cashflows on a single instrument.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_id_type** | **str** | The identifier type of the instrument. | [optional] 
**instrument_id** | **str** | The identifier for the instrument. | [optional] 
**instrument_scope** | **str** | The scope of the instrument. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**legs** | [**List[InstrumentPaymentDiaryLeg]**](InstrumentPaymentDiaryLeg.md) | Aggregated sets of Cashflows. | [optional] 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.instrument_payment_diary import InstrumentPaymentDiary
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

instrument_id_type: Optional[StrictStr] = "example_instrument_id_type"
instrument_id: Optional[StrictStr] = "example_instrument_id"
instrument_scope: Optional[StrictStr] = "example_instrument_scope"
version: Optional[Version] = None
legs: Optional[List[InstrumentPaymentDiaryLeg]] = # Replace with your value
href: Optional[StrictStr] = "example_href"
links: Optional[List[Link]] = None
instrument_payment_diary_instance = InstrumentPaymentDiary(instrument_id_type=instrument_id_type, instrument_id=instrument_id, instrument_scope=instrument_scope, version=version, legs=legs, href=href, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

