# CreateMatchingRulesetRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | The name of the matching ruleset. | 
**rec_type** | **str** | The type of reconciliation to perform. Available values: Holding, CashHolding, Valuation, InputTransaction, OutputTransaction, SettlementActivity. | 
**dataset_schemas** | [**RecDatasetSchemas**](RecDatasetSchemas.md) |  | [optional] 
**filters** | [**GroupReconciliationFilters**](GroupReconciliationFilters.md) |  | [optional] 
**core_rules** | [**List[CoreMatchingRule]**](CoreMatchingRule.md) | The core comparison rules evaluated as derivation formulae against each side of the reconciliation. | 
**aggregate_rules** | [**List[AggregateMatchingRule]**](AggregateMatchingRule.md) | The aggregate comparison rules evaluated as derivation formulae against values on each side of the reconciliation and operation to aggregate those values. | 
**core_tolerances** | [**List[ToleranceBase]**](ToleranceBase.md) | Tolerance configurations applied to core rule matching, in the specified order. | [optional] 
**aggregate_tolerances** | [**List[ToleranceBase]**](ToleranceBase.md) | Tolerance configurations applied to aggregate rule matching. | [optional] 
**allow_partial_matching** | **bool** | Whether to permit partial matches when applying rules. | [optional] 
**supplemental_attributes** | [**List[SupplementalAttribute]**](SupplementalAttribute.md) | Supplemental attributes that decorate reconciliation results with additional values without participating in the reconciliation itself. | [optional] 
## Example

```python
from lusid.models.create_matching_ruleset_request import CreateMatchingRulesetRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: ResourceId
display_name: StrictStr = "example_display_name"
rec_type: StrictStr = "example_rec_type"
dataset_schemas: Optional[RecDatasetSchemas] = # Replace with your value
filters: Optional[GroupReconciliationFilters] = None
core_rules: List[CoreMatchingRule] = # Replace with your value
aggregate_rules: List[AggregateMatchingRule] = # Replace with your value
core_tolerances: Optional[List[ToleranceBase]] = # Replace with your value
aggregate_tolerances: Optional[List[ToleranceBase]] = # Replace with your value
allow_partial_matching: Optional[StrictBool] = # Replace with your value
allow_partial_matching:Optional[StrictBool] = None
supplemental_attributes: Optional[List[SupplementalAttribute]] = # Replace with your value
create_matching_ruleset_request_instance = CreateMatchingRulesetRequest(id=id, display_name=display_name, rec_type=rec_type, dataset_schemas=dataset_schemas, filters=filters, core_rules=core_rules, aggregate_rules=aggregate_rules, core_tolerances=core_tolerances, aggregate_tolerances=aggregate_tolerances, allow_partial_matching=allow_partial_matching, supplemental_attributes=supplemental_attributes)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

