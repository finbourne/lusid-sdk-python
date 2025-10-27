# TransactionTypeDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The scope in which the TransactionType was resolved. If the portfolio has a TransactionTypeScope, this will have been used. Otherwise the default scope will have been used. | 
**source** | **str** | The source in which the TransactionType was resolved. | 
**type** | **str** | The resolved TransactionType. More information on TransactionType resolution can be found at https://support.lusid.com/docs/how-does-lusid-resolve-transactions-to-transaction-types | 
## Example

```python
from lusid.models.transaction_type_details import TransactionTypeDetails
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

scope: StrictStr = "example_scope"
source: StrictStr = "example_source"
type: StrictStr = "example_type"
transaction_type_details_instance = TransactionTypeDetails(scope=scope, source=source, type=type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

