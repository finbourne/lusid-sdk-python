# InvestmentPortfolio

An Investment Portfolio of an Investment Account.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A client-defined key used to identify the Investment Portfolio, unique within the Investment Account | [optional] 
**scope** | **str** | The scope of the Investment Portfolio | [optional] 
**identifiers** | **Dict[str, str]** | The code identifier of the Investment Portfolio | [optional] 
**entity_unique_id** | **str** | The unique Portfolio entity identifier | [optional] 
**portfolio** | [**Portfolio**](Portfolio.md) |  | [optional] 
## Example

```python
from lusid.models.investment_portfolio import InvestmentPortfolio
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr

key: Optional[StrictStr] = "example_key"
scope: Optional[StrictStr] = "example_scope"
identifiers: Optional[Dict[str, StrictStr]] = # Replace with your value
entity_unique_id: Optional[StrictStr] = "example_entity_unique_id"
portfolio: Optional[Portfolio] = None
investment_portfolio_instance = InvestmentPortfolio(key=key, scope=scope, identifiers=identifiers, entity_unique_id=entity_unique_id, portfolio=portfolio)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

