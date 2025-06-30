# ValuationPointResourceListOfAccountedTransaction

ResourceList with extra header fields used by the various ValuationPoint endpoints for returning additional context related to the list of results.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_valuation_point** | [**DiaryEntry**](DiaryEntry.md) |  | [optional] 
**version** | [**Version**](Version.md) |  | 
**values** | [**List[AccountedTransaction]**](AccountedTransaction.md) |  | 
**href** | **str** |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.valuation_point_resource_list_of_accounted_transaction import ValuationPointResourceListOfAccountedTransaction
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

start_valuation_point: Optional[DiaryEntry] = # Replace with your value
version: Version = # Replace with your value
values: conlist(AccountedTransaction) = # Replace with your value
href: Optional[StrictStr] = "example_href"
next_page: Optional[StrictStr] = "example_next_page"
previous_page: Optional[StrictStr] = "example_previous_page"
links: Optional[conlist(Link)] = None
valuation_point_resource_list_of_accounted_transaction_instance = ValuationPointResourceListOfAccountedTransaction(start_valuation_point=start_valuation_point, version=version, values=values, href=href, next_page=next_page, previous_page=previous_page, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

