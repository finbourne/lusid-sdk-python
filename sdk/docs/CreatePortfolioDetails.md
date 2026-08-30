# CreatePortfolioDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**corporate_action_source_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**tax_lot_selection_cost_basis** | **str** | The cost figure that cost-referencing accounting methods evaluate when selecting tax lots for a disposal. This can be: Cost or AmortisedCost. If not supplied, the portfolio&#39;s current value is left unchanged; supply Default to reset it. Available values: Cost, AmortisedCost. | [optional] 
## Example

```python
from lusid.models.create_portfolio_details import CreatePortfolioDetails
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

corporate_action_source_id: Optional[ResourceId] = # Replace with your value
tax_lot_selection_cost_basis: Optional[StrictStr] = "example_tax_lot_selection_cost_basis"
create_portfolio_details_instance = CreatePortfolioDetails(corporate_action_source_id=corporate_action_source_id, tax_lot_selection_cost_basis=tax_lot_selection_cost_basis)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

