# PackTransactionType

A transaction type carried by a partnership configuration pack.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The transaction type. | 
**description** | **str** | A description of the transaction type. | [optional] 
**debit_account** | **str** | The account debited. | 
**credit_account** | **str** | The account credited. | 
**direction** | **str** | The direction of the capital movement from the partner&#39;s point of view. Available values: Inflow, Outflow, Neutral. | 
## Example

```python
from lusid.models.pack_transaction_type import PackTransactionType
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

type: StrictStr = "example_type"
description: Optional[StrictStr] = "example_description"
debit_account: StrictStr = "example_debit_account"
credit_account: StrictStr = "example_credit_account"
direction: StrictStr = "example_direction"
pack_transaction_type_instance = PackTransactionType(type=type, description=description, debit_account=debit_account, credit_account=credit_account, direction=direction)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

