# TransactionSetConfigurationData

A collection of the data required to configure transaction types..
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_configs** | [**List[TransactionConfigurationData]**](TransactionConfigurationData.md) | Collection of transaction type models | 
**side_definitions** | [**List[SideConfigurationData]**](SideConfigurationData.md) | Collection of side definitions | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.transaction_set_configuration_data import TransactionSetConfigurationData
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

transaction_configs: List[TransactionConfigurationData] = # Replace with your value
side_definitions: Optional[List[SideConfigurationData]] = # Replace with your value
links: Optional[List[Link]] = None
transaction_set_configuration_data_instance = TransactionSetConfigurationData(transaction_configs=transaction_configs, side_definitions=side_definitions, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

