# UpsertInvestmentAccountRequest

Request to create or update an investor record
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The scope in which the Investment Account lies. | 
**identifiers** | [**Dict[str, ModelProperty]**](ModelProperty.md) | Unique client-defined identifiers of the Investment Account. | 
**display_name** | **str** | The display name of the Investment Account | 
**description** | **str** | The description of the Investment Account | [optional] 
**account_type** | **str** | The type of the of the Investment Account. | 
**account_holders** | [**List[AccountHolderIdentifier]**](AccountHolderIdentifier.md) | The identification of the account holders associated with this investment account | [optional] 
**investment_portfolios** | [**List[InvestmentPortfolioIdentifier]**](InvestmentPortfolioIdentifier.md) | The identification of the investment portfolios associated with this investment account | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties associated to the Investment Account. | [optional] 
## Example

```python
from lusid.models.upsert_investment_account_request import UpsertInvestmentAccountRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist, constr, validator

scope: StrictStr = "example_scope"
identifiers: Dict[str, ModelProperty] = # Replace with your value
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
account_type: StrictStr = "example_account_type"
account_holders: Optional[conlist(AccountHolderIdentifier)] = # Replace with your value
investment_portfolios: Optional[conlist(InvestmentPortfolioIdentifier)] = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
upsert_investment_account_request_instance = UpsertInvestmentAccountRequest(scope=scope, identifiers=identifiers, display_name=display_name, description=description, account_type=account_type, account_holders=account_holders, investment_portfolios=investment_portfolios, properties=properties)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

