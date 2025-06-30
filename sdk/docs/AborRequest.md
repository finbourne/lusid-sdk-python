# AborRequest

The request used to create an Abor.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code given for the Abor. | 
**display_name** | **str** | The name of the Abor. | 
**description** | **str** | The description for the Abor. | [optional] 
**portfolio_ids** | [**List[PortfolioEntityId]**](PortfolioEntityId.md) | The list with the portfolio ids which are part of the Abor. Note: These must all have the same base currency. | 
**abor_configuration_id** | [**ResourceId**](ResourceId.md) |  | 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties for the Abor. | [optional] 
## Example

```python
from lusid.models.abor_request import AborRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist, constr, validator

code: StrictStr = "example_code"
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
portfolio_ids: conlist(PortfolioEntityId) = # Replace with your value
abor_configuration_id: ResourceId = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
abor_request_instance = AborRequest(code=code, display_name=display_name, description=description, portfolio_ids=portfolio_ids, abor_configuration_id=abor_configuration_id, properties=properties)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

