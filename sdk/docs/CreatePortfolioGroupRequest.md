# CreatePortfolioGroupRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code that the portfolio group will be created with. Together with the scope this uniquely identifies the portfolio group. | 
**created** | **datetime** | The effective datetime at which the portfolio group was created. Defaults to the current LUSID system datetime if not specified. | [optional] 
**values** | [**List[ResourceId]**](ResourceId.md) | The resource identifiers of the portfolios to be contained within the portfolio group. | [optional] 
**sub_groups** | [**List[ResourceId]**](ResourceId.md) | The resource identifiers of the portfolio groups to be contained within the portfolio group as sub groups. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of unique group properties to add to the portfolio group. Each property must be from the &#39;PortfolioGroup&#39; domain and should be identified by its key which has the format {domain}/{scope}/{code}, e.g. &#39;PortfolioGroup/Manager/Id&#39;. These properties must be pre-defined. | [optional] 
**display_name** | **str** | The name of the portfolio group. | 
**description** | **str** | A long form description of the portfolio group. | [optional] 
## Example

```python
from lusid.models.create_portfolio_group_request import CreatePortfolioGroupRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr
from datetime import datetime
code: StrictStr = "example_code"
created: Optional[datetime] = # Replace with your value
values: Optional[conlist(ResourceId)] = # Replace with your value
sub_groups: Optional[conlist(ResourceId)] = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
create_portfolio_group_request_instance = CreatePortfolioGroupRequest(code=code, created=created, values=values, sub_groups=sub_groups, properties=properties, display_name=display_name, description=description)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

