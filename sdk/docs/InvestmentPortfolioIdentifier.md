# InvestmentPortfolioIdentifier

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A client-defined key used to identify the Investment Portfolio, unique within the Investment Account | 
**scope** | **str** | The scope of the Investment Portfolio. | 
**identifiers** | **Dict[str, Optional[str]]** | The code identifier of the Investment Portfolio. | 
## Example

```python
from lusid.models.investment_portfolio_identifier import InvestmentPortfolioIdentifier
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

key: StrictStr = "example_key"
scope: StrictStr = "example_scope"
identifiers: Dict[str, Optional[StrictStr]] = # Replace with your value
investment_portfolio_identifier_instance = InvestmentPortfolioIdentifier(key=key, scope=scope, identifiers=identifiers)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

