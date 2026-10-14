# CollateralAgreementApplicability

The portfolios a collateral agreement currently covers, according to its applicability filter.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**applicability_filter** | **str** | The applicability filter that was evaluated. Only its clauses on portfolio fields are applied to select the portfolios returned. | 
**portfolios** | [**List[ResourceId]**](ResourceId.md) | The portfolios matching the applicability filter, up to the requested limit. | 
**has_more_portfolios** | **bool** | Whether more portfolios match the filter than were returned. | 
## Example

```python
from lusid.models.collateral_agreement_applicability import CollateralAgreementApplicability
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: ResourceId
applicability_filter: StrictStr = "example_applicability_filter"
portfolios: List[ResourceId] = # Replace with your value
has_more_portfolios: StrictBool = # Replace with your value
has_more_portfolios:StrictBool = True
collateral_agreement_applicability_instance = CollateralAgreementApplicability(id=id, applicability_filter=applicability_filter, portfolios=portfolios, has_more_portfolios=has_more_portfolios)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

