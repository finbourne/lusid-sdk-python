# ValuationPointOverview

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**diary_entry_code** | **str** | The code for the Valuation Point. | 
**diary_entry_variant** | **str** | The Variant for the Valuation Point. Together with the valuation point code marks the unique branch for the NavType. | [optional] 
**effective_from** | **datetime** | The effective time of the last Valuation Point. | 
**effective_to** | **datetime** | The effective time of the current Valuation Point. | 
**query_as_at** | **datetime** | The query time of the Valuation Point. Defaults to latest. | [optional] 
**type** | **str** | The type of the diary entry. This is &#39;ValuationPoint&#39;. | 
**status** | **str** | The status of the Valuation Point. Can be &#39;Estimate&#39;, &#39;Candidate&#39; or &#39;Final&#39;. | 
**gav** | **float** | The Gross Asset Value of the Fund or Share Class at the Valuation Point. This is effectively a summation of all Trial balance entries linked to accounts of types &#39;Asset&#39; and &#39;Liabilities&#39;. | 
**nav** | **float** | The Net Asset Value of the Fund or Share Class at the Valuation Point. This represents the GAV with any fees applied in the period. | 
**holdings_as_at_override** | **datetime** | The optional AsAt Override to use for building holdings in the Valuation Point. Defaults to Latest. | [optional] 
**valuations_as_at_override** | **datetime** | The optional AsAt Override to use for performing valuations in the Valuation Point. Defaults to Latest. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The Fee properties. These will be from the &#39;Fee&#39; domain. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.valuation_point_overview import ValuationPointOverview
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
diary_entry_code: StrictStr = "example_diary_entry_code"
diary_entry_variant: Optional[StrictStr] = "example_diary_entry_variant"
effective_from: datetime = # Replace with your value
effective_to: datetime = # Replace with your value
query_as_at: Optional[datetime] = # Replace with your value
type: StrictStr = "example_type"
status: StrictStr = "example_status"
gav: Union[StrictFloat, StrictInt] = # Replace with your value
nav: Union[StrictFloat, StrictInt] = # Replace with your value
holdings_as_at_override: Optional[datetime] = # Replace with your value
valuations_as_at_override: Optional[datetime] = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
links: Optional[List[Link]] = None
valuation_point_overview_instance = ValuationPointOverview(href=href, diary_entry_code=diary_entry_code, diary_entry_variant=diary_entry_variant, effective_from=effective_from, effective_to=effective_to, query_as_at=query_as_at, type=type, status=status, gav=gav, nav=nav, holdings_as_at_override=holdings_as_at_override, valuations_as_at_override=valuations_as_at_override, properties=properties, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

