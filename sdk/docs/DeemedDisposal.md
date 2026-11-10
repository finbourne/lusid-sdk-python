# DeemedDisposal

Settings for the deemed disposal a NAV type books at period close. When enabled, the in-scope holdings are  treated as sold and immediately re-acquired at market value, realising their unrealised gain against the  chosen cost base.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether the Nav Type books a deemed disposal at period close. When true, in-scope holdings are treated as sold and immediately re-acquired at market value, realising their unrealised gain. | 
**cost_base** | **str** | The cost the deemed disposal realises against: Book or Tax. Defaults to Book. Book: rebases book cost to base value and posts the movement as realised FX; it moves the portfolio&#39;s cost, so it is only valid on the primary Nav Type. Tax: writes a tax cost equal to market value and spreads the deemed gain since the prior tax cost. Available values: Book, Tax. | [optional] 
**holdings_filter** | **str** | An optional filter selecting which holdings are deemed disposed of at period close. Omit it for the cost base&#39;s default: under Book, every non-base-currency monetary item (cash, receivables, payables, accruals). Tax has no default yet, so set a filter. | [optional] 
**transaction_type_code** | **str** | An optional transaction type, in the Nav Type&#39;s transaction type scope, that the deemed disposal transactions are booked with. Omit it to use the domain default deemed disposal transaction type. | [optional] 
## Example

```python
from lusid.models.deemed_disposal import DeemedDisposal
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

enabled: StrictBool = # Replace with your value
enabled:StrictBool = True
cost_base: Optional[StrictStr] = "example_cost_base"
holdings_filter: Optional[StrictStr] = "example_holdings_filter"
transaction_type_code: Optional[StrictStr] = "example_transaction_type_code"
deemed_disposal_instance = DeemedDisposal(enabled=enabled, cost_base=cost_base, holdings_filter=holdings_filter, transaction_type_code=transaction_type_code)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

