# ReconciliationConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | [**ReconciliationSideConfiguration**](ReconciliationSideConfiguration.md) |  | [optional] 
**right** | [**ReconciliationSideConfiguration**](ReconciliationSideConfiguration.md) |  | [optional] 
**mapping_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
## Example

```python
from lusid.models.reconciliation_configuration import ReconciliationConfiguration
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field

left: Optional[ReconciliationSideConfiguration] = None
right: Optional[ReconciliationSideConfiguration] = None
mapping_id: Optional[ResourceId] = # Replace with your value
reconciliation_configuration_instance = ReconciliationConfiguration(left=left, right=right, mapping_id=mapping_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

