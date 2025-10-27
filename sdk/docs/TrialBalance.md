# TrialBalance

A TrialBalance entity.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**general_ledger_account_code** | **str** | The Account code that the trial balance results have been grouped against. | 
**description** | **str** | The description of the record. | [optional] 
**levels** | **List[str]** | The levels that have been derived from the specified General Ledger Profile. | 
**account_type** | **str** | The account type attributed to the record. | 
**local_currency** | **str** | The local currency for the amounts specified. Defaults to base currency if multiple different currencies present in the grouped line. | 
**opening** | [**MultiCurrencyAmounts**](MultiCurrencyAmounts.md) |  | 
**closing** | [**MultiCurrencyAmounts**](MultiCurrencyAmounts.md) |  | 
**debit** | [**MultiCurrencyAmounts**](MultiCurrencyAmounts.md) |  | 
**credit** | [**MultiCurrencyAmounts**](MultiCurrencyAmounts.md) |  | 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | Properties found on the mapped &#39;Account&#39;, as specified in request. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.trial_balance import TrialBalance
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

general_ledger_account_code: StrictStr = "example_general_ledger_account_code"
description: Optional[StrictStr] = "example_description"
levels: List[StrictStr] = # Replace with your value
account_type: StrictStr = "example_account_type"
local_currency: StrictStr = "example_local_currency"
opening: MultiCurrencyAmounts
closing: MultiCurrencyAmounts
debit: MultiCurrencyAmounts
credit: MultiCurrencyAmounts
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
links: Optional[List[Link]] = None
trial_balance_instance = TrialBalance(general_ledger_account_code=general_ledger_account_code, description=description, levels=levels, account_type=account_type, local_currency=local_currency, opening=opening, closing=closing, debit=debit, credit=credit, properties=properties, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

