# PortfolioContentsRecDefinitionDetails

A definition reconciling the contents of LUSID portfolios on at least one side, with a relational dataset  permitted on the other.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left_portfolio_sources** | [**List[RecDefSource]**](RecDefSource.md) | The portfolios, portfolio groups and funds contributing to the left side. Empty when the left side draws on relational data instead, which requires every ruleset to declare relational data for that side. Both sides cannot be empty. | 
**right_portfolio_sources** | [**List[RecDefSource]**](RecDefSource.md) | The portfolios, portfolio groups and funds contributing to the right side. Empty when the right side draws on relational data instead, which requires every ruleset to declare relational data for that side. Both sides cannot be empty. | 
**valuation_recipes** | [**RecDefRecipeIds**](RecDefRecipeIds.md) |  | [optional] 
**currencies** | [**RecDefCurrencies**](RecDefCurrencies.md) |  | [optional] 
**rulesets** | [**List[RecDefRuleset]**](RecDefRuleset.md) | The types of reconciliation included in the group, each naming the matching ruleset that drives it. At least one entry is required, and each rec type may appear at most once. | 
**definition_type** | **str** | What this definition reconciles, and so which shape of details it carries. Available values: PortfolioContents, LusidEntity, External. | 
## Example

```python
from lusid.models.portfolio_contents_rec_definition_details import PortfolioContentsRecDefinitionDetails
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

left_portfolio_sources: List[RecDefSource] = # Replace with your value
right_portfolio_sources: List[RecDefSource] = # Replace with your value
valuation_recipes: Optional[RecDefRecipeIds] = # Replace with your value
currencies: Optional[RecDefCurrencies] = None
rulesets: List[RecDefRuleset] = # Replace with your value
definition_type: StrictStr = "example_definition_type"
portfolio_contents_rec_definition_details_instance = PortfolioContentsRecDefinitionDetails(left_portfolio_sources=left_portfolio_sources, right_portfolio_sources=right_portfolio_sources, valuation_recipes=valuation_recipes, currencies=currencies, rulesets=rulesets, definition_type=definition_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

