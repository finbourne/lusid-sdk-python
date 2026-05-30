# PreviousValuationPoint

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valuation_point_code** | **str** | The code of the Valuation Point. | 
**name** | **str** | Identifiable Name assigned to the Valuation Point. | [optional] 
**effective_at** | **datetime** | The effective time of the Valuation Point. | 
**query_as_at** | **datetime** | The AsAt time of the Valuation Point. This is the AsAt time that will be used when requests are made using the entry. | 
**holdings_as_at** | **datetime** | The AsAt time used for building holdings in the Valuation Point. | [optional] 
**valuation_as_at** | **datetime** | The AsAt time used for performing valuations in the Valuation Point. | [optional] 
## Example

```python
from lusid.models.previous_valuation_point import PreviousValuationPoint
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

valuation_point_code: StrictStr = "example_valuation_point_code"
name: Optional[StrictStr] = "example_name"
effective_at: datetime = # Replace with your value
query_as_at: datetime = # Replace with your value
holdings_as_at: Optional[datetime] = # Replace with your value
valuation_as_at: Optional[datetime] = # Replace with your value
previous_valuation_point_instance = PreviousValuationPoint(valuation_point_code=valuation_point_code, name=name, effective_at=effective_at, query_as_at=query_as_at, holdings_as_at=holdings_as_at, valuation_as_at=valuation_as_at)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

