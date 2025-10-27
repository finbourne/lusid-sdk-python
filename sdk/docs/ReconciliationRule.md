# ReconciliationRule

Base class for representing reconciliation rules in LUSID.  Reconciliation rules describe how a comparison between two items in the reconciliation should be performed and what constitutes equality.  This does not influence WHAT constitutes a match, but only whether once a line has been matched whether an item within it matches another item.  If a rule is not given for an item, it will default to equality comparison.  This base class should not be directly instantiated; each supported ReconciliationRuleType has a corresponding inherited class.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_type** | **str** | The available values are: ReconcileNumericRule, ReconcileDateTimeRule, ReconcileStringRule, ReconcileExact | 
## Example

```python
from lusid.models.reconciliation_rule import ReconciliationRule
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

rule_type: StrictStr = "example_rule_type"
reconciliation_rule_instance = ReconciliationRule(rule_type=rule_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

