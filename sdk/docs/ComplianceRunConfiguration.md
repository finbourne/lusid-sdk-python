# ComplianceRunConfiguration

Specification object for the configuration parameters of a compliance run
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pre_trade_configuration** | [**PreTradeConfiguration**](PreTradeConfiguration.md) |  | 
## Example

```python
from lusid.models.compliance_run_configuration import ComplianceRunConfiguration
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field

pre_trade_configuration: PreTradeConfiguration = # Replace with your value
compliance_run_configuration_instance = ComplianceRunConfiguration(pre_trade_configuration=pre_trade_configuration)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

