# FundRequest

The request used to create a Fund.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code given for the Fund. | 
**display_name** | **str** | The name of the Fund. | [optional] 
**description** | **str** | A description for the Fund. | [optional] 
**fund_configuration_id** | [**ResourceId**](ResourceId.md) |  | 
**abor_id** | [**ResourceId**](ResourceId.md) |  | 
**share_class_instrument_scopes** | **List[str]** | The scopes in which the instruments lie, currently limited to one. | [optional] 
**share_class_instruments** | [**List[InstrumentResolutionDetail]**](InstrumentResolutionDetail.md) | Details the user-provided instrument identifiers and the instrument resolved from them. | [optional] 
**type** | **str** | The type of fund; &#39;Standalone&#39;, &#39;Master&#39; or &#39;Feeder&#39; | 
**inception_date** | **datetime** | Inception date of the Fund | 
**decimal_places** | **int** | Number of decimal places for reporting | [optional] 
**year_end_date** | [**DayMonth**](DayMonth.md) |  | 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties for the Fund. | [optional] 
## Example

```python
from lusid.models.fund_request import FundRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

code: StrictStr = "example_code"
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
fund_configuration_id: ResourceId = # Replace with your value
abor_id: ResourceId = # Replace with your value
share_class_instrument_scopes: Optional[List[StrictStr]] = # Replace with your value
share_class_instruments: Optional[List[InstrumentResolutionDetail]] = # Replace with your value
type: StrictStr = "example_type"
inception_date: datetime = # Replace with your value
decimal_places: Optional[StrictInt] = # Replace with your value
decimal_places: Optional[StrictInt] = None
year_end_date: DayMonth = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
fund_request_instance = FundRequest(code=code, display_name=display_name, description=description, fund_configuration_id=fund_configuration_id, abor_id=abor_id, share_class_instrument_scopes=share_class_instrument_scopes, share_class_instruments=share_class_instruments, type=type, inception_date=inception_date, decimal_places=decimal_places, year_end_date=year_end_date, properties=properties)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

