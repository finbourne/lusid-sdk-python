# TransactionFeeCapitalisation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capitalisation** | **str** | Whether the transaction fee should be capitalised, not capitalised, or conditionally capitalised. The allowed values are Capitalised, NonCapitalised, Conditional. | [optional] 
**capitalised_condition** | **str** | The condition that determines whether the fee is capitalised when applied to the transaction. Required only when Capitalisation is &#39;Conditional&#39;. | [optional] 
## Example

```python
from lusid.models.transaction_fee_capitalisation import TransactionFeeCapitalisation
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

capitalisation: Optional[StrictStr] = "example_capitalisation"
capitalised_condition: Optional[StrictStr] = "example_capitalised_condition"
transaction_fee_capitalisation_instance = TransactionFeeCapitalisation(capitalisation=capitalisation, capitalised_condition=capitalised_condition)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

