# CreateRecDefinitionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | The name of the rec definition. | 
**description** | **str** | A description of the rec definition. | [optional] 
**definition_type** | **str** | What this definition reconciles, naming the kind of dataset that must be present on at least one side. One of: PortfolioContents, LusidEntity, RelationalData. Only PortfolioContents is currently supported. Available values: PortfolioContents, LusidEntity, RelationalData. | 
**side_names** | [**RecDefSideNames**](RecDefSideNames.md) |  | [optional] 
**left_portfolio_sources** | [**List[RecDefSource]**](RecDefSource.md) | The portfolios, portfolio groups and funds contributing to the left side. Empty when the left side draws on relational data instead, which requires every ruleset to declare relational data for that side. Both sides cannot be empty. | [optional] 
**right_portfolio_sources** | [**List[RecDefSource]**](RecDefSource.md) | The portfolios, portfolio groups and funds contributing to the right side. Empty when the right side draws on relational data instead, which requires every ruleset to declare relational data for that side. Both sides cannot be empty. | [optional] 
**valuation_recipes** | [**RecDefRecipeIds**](RecDefRecipeIds.md) |  | [optional] 
**currencies** | [**RecDefCurrencies**](RecDefCurrencies.md) |  | [optional] 
**rulesets** | [**List[RecDefRuleset]**](RecDefRuleset.md) | The types of reconciliation included in the group, each naming the matching ruleset that drives it. At least one entry is required, and each rec type may appear at most once. | 
## Example

```python
from lusid.models.create_rec_definition_request import CreateRecDefinitionRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: ResourceId
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
definition_type: StrictStr = "example_definition_type"
side_names: Optional[RecDefSideNames] = # Replace with your value
left_portfolio_sources: Optional[List[RecDefSource]] = # Replace with your value
right_portfolio_sources: Optional[List[RecDefSource]] = # Replace with your value
valuation_recipes: Optional[RecDefRecipeIds] = # Replace with your value
currencies: Optional[RecDefCurrencies] = None
rulesets: List[RecDefRuleset] = # Replace with your value
create_rec_definition_request_instance = CreateRecDefinitionRequest(id=id, display_name=display_name, description=description, definition_type=definition_type, side_names=side_names, left_portfolio_sources=left_portfolio_sources, right_portfolio_sources=right_portfolio_sources, valuation_recipes=valuation_recipes, currencies=currencies, rulesets=rulesets)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

