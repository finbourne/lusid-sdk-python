# TransactionSetConfigurationDataRequest

A bundle of requests to configure a set of transaction types.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_config_requests** | [**List[TransactionConfigurationDataRequest]**](TransactionConfigurationDataRequest.md) | Collection of transaction type models | 
**side_config_requests** | [**List[SideConfigurationDataRequest]**](SideConfigurationDataRequest.md) | Collection of side definition requests. | [optional] 
## Example

```python
from lusid.models.transaction_set_configuration_data_request import TransactionSetConfigurationDataRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist

transaction_config_requests: conlist(TransactionConfigurationDataRequest) = # Replace with your value
side_config_requests: Optional[conlist(SideConfigurationDataRequest)] = # Replace with your value
transaction_set_configuration_data_request_instance = TransactionSetConfigurationDataRequest(transaction_config_requests=transaction_config_requests, side_config_requests=side_config_requests)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

