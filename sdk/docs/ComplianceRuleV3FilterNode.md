# ComplianceRuleV3FilterNode

A node in a rule's filter tree: either a group combining child nodes with all/any, or a leaf condition.  The concrete kind is named by the FilterNodeType property.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_node_type** | **str** | Available values: ComplianceRuleV3FilterGroup, ComplianceRuleV3FilterCondition. | 
## Example

```python
from lusid.models.compliance_rule_v3_filter_node import ComplianceRuleV3FilterNode
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

filter_node_type: StrictStr = "example_filter_node_type"
compliance_rule_v3_filter_node_instance = ComplianceRuleV3FilterNode(filter_node_type=filter_node_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

