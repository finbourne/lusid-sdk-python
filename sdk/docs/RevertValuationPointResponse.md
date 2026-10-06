# RevertValuationPointResponse

A Valuation Point reverted to Estimate, with all of its variants. Any variant that finalising the Valuation Point  had rejected is brought back as an Estimate by the revert, and is reported here alongside it.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**valuation_point_code** | **str** | The code of the Valuation Point. | [optional] 
**nav_type_code** | **str** | The navTypeCode of the Fund Calendar Entry. This is the code of the NAV type that this Calendar Entry is associated with. | [optional] 
**status** | **str** | The status of the Valuation Point. Available values: Undefined, Estimate, Final, Candidate, Rejected, Unofficial. | 
**apply_clear_down** | **bool** | Indicates whether a clear down was applied when the Valuation Point was created. | [optional] 
**effective_at** | **datetime** | The effective time of the Valuation Point. | 
**previous** | [**PreviousValuationPoint**](PreviousValuationPoint.md) |  | [optional] 
**variants** | [**List[EstimateVariant]**](EstimateVariant.md) | The variants of the Estimate Valuation Point.  | [optional] 
**staged_modifications** | [**StagedModificationsInfo**](StagedModificationsInfo.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.revert_valuation_point_response import RevertValuationPointResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
valuation_point_code: Optional[StrictStr] = "example_valuation_point_code"
nav_type_code: Optional[StrictStr] = "example_nav_type_code"
status: StrictStr = "example_status"
apply_clear_down: Optional[StrictBool] = # Replace with your value
apply_clear_down:Optional[StrictBool] = None
effective_at: datetime = # Replace with your value
previous: Optional[PreviousValuationPoint] = None
variants: Optional[List[EstimateVariant]] = # Replace with your value
staged_modifications: Optional[StagedModificationsInfo] = # Replace with your value
links: Optional[List[Link]] = None
revert_valuation_point_response_instance = RevertValuationPointResponse(href=href, valuation_point_code=valuation_point_code, nav_type_code=nav_type_code, status=status, apply_clear_down=apply_clear_down, effective_at=effective_at, previous=previous, variants=variants, staged_modifications=staged_modifications, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

