# SetAmortisationRulesRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rules_interval** | [**RulesInterval**](RulesInterval.md) |  | 
## Example

```python
from lusid.models.set_amortisation_rules_request import SetAmortisationRulesRequest
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field

rules_interval: RulesInterval = # Replace with your value
set_amortisation_rules_request_instance = SetAmortisationRulesRequest(rules_interval=rules_interval)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

