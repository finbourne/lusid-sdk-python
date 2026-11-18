# PackTypeContract

The register deltas a transaction type must carry for the partner register to read right.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The transaction type the contract is for. | 
**required_deltas** | [**List[PackRegisterDelta]**](PackRegisterDelta.md) | The register balance deltas the type must carry, counted with repeats. | 
**optional_deltas** | [**List[PackRegisterDelta]**](PackRegisterDelta.md) | The register balance deltas the type may carry, each at most once, in the direction given and from the source given. | 
## Example

```python
from lusid.models.pack_type_contract import PackTypeContract
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

type: StrictStr = "example_type"
required_deltas: List[PackRegisterDelta] = # Replace with your value
optional_deltas: List[PackRegisterDelta] = # Replace with your value
pack_type_contract_instance = PackTypeContract(type=type, required_deltas=required_deltas, optional_deltas=optional_deltas)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

