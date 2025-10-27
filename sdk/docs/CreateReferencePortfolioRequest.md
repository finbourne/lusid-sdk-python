# CreateReferencePortfolioRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the reference portfolio. | 
**description** | **str** | A long form text description of the portfolio. | [optional] 
**code** | **str** | Unique identifier for the portfolio. | 
**created** | **datetime** | The original creation date, defaults to today if not specified when creating a portfolio. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | Portfolio properties to add to the portfolio. | [optional] 
**instrument_scopes** | **List[str]** | Instrument Scopes. | [optional] 
**base_currency** | **str** | The base currency of the transaction portfolio in ISO 4217 currency code format. | [optional] 
## Example

```python
from lusid.models.create_reference_portfolio_request import CreateReferencePortfolioRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
code: StrictStr = "example_code"
created: Optional[datetime] = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
instrument_scopes: Optional[List[StrictStr]] = # Replace with your value
base_currency: Optional[StrictStr] = "example_base_currency"
create_reference_portfolio_request_instance = CreateReferencePortfolioRequest(display_name=display_name, description=description, code=code, created=created, properties=properties, instrument_scopes=instrument_scopes, base_currency=base_currency)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

