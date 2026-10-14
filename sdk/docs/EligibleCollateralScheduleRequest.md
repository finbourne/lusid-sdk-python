# EligibleCollateralScheduleRequest

The request used to create an Eligible Collateral Schedule.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code of the Eligible Collateral Schedule. | 
**description** | **str** | A description of the Eligible Collateral Schedule. Optional. | [optional] 
**rows** | [**List[EligibleCollateralRowRequest]**](EligibleCollateralRowRequest.md) | The classes of collateral that may be posted, each with the valuation percentage it is accepted at. At least one and at most 200 rows. | 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties to decorate onto the Eligible Collateral Schedule. Filterable. | [optional] 
**effective_at** | **datetime** | The effective datetime from which the Eligible Collateral Schedule applies. Defaults to the beginning of time if not specified, so that the schedule is visible at every effective datetime. | [optional] 
## Example

```python
from lusid.models.eligible_collateral_schedule_request import EligibleCollateralScheduleRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

code: StrictStr = "example_code"
description: Optional[StrictStr] = "example_description"
rows: List[EligibleCollateralRowRequest] = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
effective_at: Optional[datetime] = # Replace with your value
eligible_collateral_schedule_request_instance = EligibleCollateralScheduleRequest(code=code, description=description, rows=rows, properties=properties, effective_at=effective_at)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

