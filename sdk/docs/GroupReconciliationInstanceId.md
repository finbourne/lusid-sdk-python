# GroupReconciliationInstanceId

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_id_type** | **str** | Type of the reconciliation run, manual or automatic (via the workflow). \&quot;Manual\&quot; | \&quot;WorkflowServiceTaskId\&quot; | 
**instance_id_value** | **str** | Reconciliation run identifier: a manually-provided key or taskId. | 
## Example

```python
from lusid.models.group_reconciliation_instance_id import GroupReconciliationInstanceId
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

instance_id_type: StrictStr = "example_instance_id_type"
instance_id_value: StrictStr = "example_instance_id_value"
group_reconciliation_instance_id_instance = GroupReconciliationInstanceId(instance_id_type=instance_id_type, instance_id_value=instance_id_value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

