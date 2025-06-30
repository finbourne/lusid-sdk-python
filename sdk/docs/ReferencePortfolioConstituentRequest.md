# ReferencePortfolioConstituentRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_identifiers** | **Dict[str, str]** | Unique instrument identifiers | 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) |  | [optional] 
**weight** | **float** |  | 
**currency** | **str** |  | [optional] 
## Example

```python
from lusid.models.reference_portfolio_constituent_request import ReferencePortfolioConstituentRequest
from typing import Any, Dict, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, StrictStr

instrument_identifiers: Dict[str, StrictStr] = # Replace with your value
properties: Optional[Dict[str, PerpetualProperty]] = None
weight: Union[StrictFloat, StrictInt] = # Replace with your value
currency: Optional[StrictStr] = "example_currency"
reference_portfolio_constituent_request_instance = ReferencePortfolioConstituentRequest(instrument_identifiers=instrument_identifiers, properties=properties, weight=weight, currency=currency)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

