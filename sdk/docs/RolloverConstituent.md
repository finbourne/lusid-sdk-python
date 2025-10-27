# RolloverConstituent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_details** | [**ContractDetails**](ContractDetails.md) |  | 
**balance_change** | **float** | Balance of the new contract holding. | 
## Example

```python
from lusid.models.rollover_constituent import RolloverConstituent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

contract_details: ContractDetails = # Replace with your value
balance_change: Union[StrictFloat, StrictInt] = # Replace with your value
rollover_constituent_instance = RolloverConstituent(contract_details=contract_details, balance_change=balance_change)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

