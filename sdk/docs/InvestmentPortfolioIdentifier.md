# InvestmentPortfolioIdentifier

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A client-defined key used to identify the Investment Portfolio, unique within the Investment Account | 
**scope** | **str** | The scope of the Investment Portfolio. | 
**identifiers** | **Dict[str, str]** | The code identifier of the Investment Portfolio. | 
## Example

```python
from lusid.models.investment_portfolio_identifier import InvestmentPortfolioIdentifier
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, StrictStr, constr, validator

key: StrictStr = "example_key"
scope: StrictStr = "example_scope"
identifiers: Dict[str, StrictStr] = # Replace with your value
investment_portfolio_identifier_instance = InvestmentPortfolioIdentifier(key=key, scope=scope, identifiers=identifiers)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

