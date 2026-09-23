# PagedResourceListOfWithholdingTaxDataset

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[WithholdingTaxDataset]**](WithholdingTaxDataset.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.paged_resource_list_of_withholding_tax_dataset import PagedResourceListOfWithholdingTaxDataset
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

next_page: Optional[StrictStr] = "example_next_page"
previous_page: Optional[StrictStr] = "example_previous_page"
values: List[WithholdingTaxDataset]
href: Optional[StrictStr] = "example_href"
links: Optional[List[Link]] = None
paged_resource_list_of_withholding_tax_dataset_instance = PagedResourceListOfWithholdingTaxDataset(next_page=next_page, previous_page=previous_page, values=values, href=href, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

