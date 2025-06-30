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
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist

transaction_configs: conlist(TransactionConfigurationData) = # Replace with your value
side_definitions: Optional[conlist(SideConfigurationData)] = # Replace with your value
links: Optional[conlist(Link)] = None
transaction_set_configuration_data_instance = TransactionSetConfigurationData(transaction_configs=transaction_configs, side_definitions=side_definitions, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

