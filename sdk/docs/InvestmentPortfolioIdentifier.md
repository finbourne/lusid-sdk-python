# InvestmentPortfolioIdentifier

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A client-defined key used to identify the Investment Portfolio, unique within the Investment Account | 
**portfolio_scope** | **str** | The scope of the Investment Portfolio. | 
**portfolio_code** | **str** | The code of the Investment Portfolio. | 
## Example

```python
from lusid.models.investment_portfolio_identifier import InvestmentPortfolioIdentifier
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr, validator

key: StrictStr = "example_key"
portfolio_scope: StrictStr = "example_portfolio_scope"
portfolio_code: StrictStr = "example_portfolio_code"
investment_portfolio_identifier_instance = InvestmentPortfolioIdentifier(key=key, portfolio_scope=portfolio_scope, portfolio_code=portfolio_code)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

