# ReferencePortfolioConstituentRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_identifiers** | **Dict[str, Optional[str]]** | Unique instrument identifiers | 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) |  | [optional] 
**weight** | **float** |  | 
**currency** | **str** |  | [optional] 
## Example

```python
from lusid.models.reference_portfolio_constituent_request import ReferencePortfolioConstituentRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

instrument_identifiers: Dict[str, Optional[StrictStr]] = # Replace with your value
properties: Optional[Dict[str, PerpetualProperty]] = None
weight: Union[StrictFloat, StrictInt]
currency: Optional[StrictStr] = "example_currency"
reference_portfolio_constituent_request_instance = ReferencePortfolioConstituentRequest(instrument_identifiers=instrument_identifiers, properties=properties, weight=weight, currency=currency)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

