# FundGroupTrialBalanceResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fund_results** | [**List[FundGroupReportResult]**](FundGroupReportResult.md) | One entry per fund and NAV type in the group: the valuation points reported, or the reason nothing was reported for it. | [optional] 
**version** | [**Version**](Version.md) |  | 
**values** | [**List[FundGroupTrialBalance]**](FundGroupTrialBalance.md) |  | 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.fund_group_trial_balance_response import FundGroupTrialBalanceResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

fund_results: Optional[List[FundGroupReportResult]] = # Replace with your value
version: Version
values: List[FundGroupTrialBalance]
href: Optional[StrictStr] = "example_href"
next_page: Optional[StrictStr] = "example_next_page"
previous_page: Optional[StrictStr] = "example_previous_page"
links: Optional[List[Link]] = None
fund_group_trial_balance_response_instance = FundGroupTrialBalanceResponse(fund_results=fund_results, version=version, values=values, href=href, next_page=next_page, previous_page=previous_page, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

