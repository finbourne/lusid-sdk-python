# RolloverConstituent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_details** | [**ContractDetails**](ContractDetails.md) |  | 
**balance_change** | **float** | Balance of the new contract holding. | 
## Example

```python
from lusid.models.rollover_constituent import RolloverConstituent
from typing import Any, Dict, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt

contract_details: ContractDetails = # Replace with your value
balance_change: Union[StrictFloat, StrictInt] = # Replace with your value
rollover_constituent_instance = RolloverConstituent(contract_details=contract_details, balance_change=balance_change)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

