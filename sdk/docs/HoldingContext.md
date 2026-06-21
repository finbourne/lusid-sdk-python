# HoldingContext

Holding context node.  Contains settings that control how LUSID handles holdings within portfolios.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_lot_level_holdings** | **bool** | Whether or not to expand the holdings to return the underlying tax-lots. Defaults to True. | [optional] 
## Example

```python
from lusid.models.holding_context import HoldingContext
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

tax_lot_level_holdings: Optional[StrictBool] = # Replace with your value
tax_lot_level_holdings:Optional[StrictBool] = None
holding_context_instance = HoldingContext(tax_lot_level_holdings=tax_lot_level_holdings)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

