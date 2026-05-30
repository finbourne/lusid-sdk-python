# ValuationPoint

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**valuation_point_code** | **str** | The code of the Valuation Point. | [optional] 
**variant** | **str** | The Variant name for the Valuation Point. | [optional] 
**name** | **str** | Identifiable Name assigned to the Valuation Point. | [optional] 
**status** | **str** | The status of the Valuation Point. Available values: Undefined, Estimate, Final, Candidate, Unofficial. | 
**apply_clear_down** | **bool** | Indicates whether a clear down was applied when the Valuation Point was created. | [optional] 
**effective_at** | **datetime** | The effective time of the Valuation Point. | 
**query_as_at** | **datetime** | The AsAt time of the Valuation Point. This is the AsAt time that will be used when requests are made using the entry. | [optional] 
**holdings_as_at** | **datetime** | The AsAt time used for building holdings in the Valuation Point. | [optional] 
**valuation_as_at** | **datetime** | The AsAt time used for performing valuations in the Valuation Point. | [optional] 
**previous** | [**PreviousValuationPoint**](PreviousValuationPoint.md) |  | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The Valuation Point properties. These are from the &#39;DiaryEntry&#39; domain. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.valuation_point import ValuationPoint
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
valuation_point_code: Optional[StrictStr] = "example_valuation_point_code"
variant: Optional[StrictStr] = "example_variant"
name: Optional[StrictStr] = "example_name"
status: StrictStr = "example_status"
apply_clear_down: Optional[StrictBool] = # Replace with your value
apply_clear_down:Optional[StrictBool] = None
effective_at: datetime = # Replace with your value
query_as_at: Optional[datetime] = # Replace with your value
holdings_as_at: Optional[datetime] = # Replace with your value
valuation_as_at: Optional[datetime] = # Replace with your value
previous: Optional[PreviousValuationPoint] = None
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
version: Optional[Version] = None
links: Optional[List[Link]] = None
valuation_point_instance = ValuationPoint(href=href, valuation_point_code=valuation_point_code, variant=variant, name=name, status=status, apply_clear_down=apply_clear_down, effective_at=effective_at, query_as_at=query_as_at, holdings_as_at=holdings_as_at, valuation_as_at=valuation_as_at, previous=previous, properties=properties, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

