# RecResult

An individual reconciliation result — the aggregate result for a set of core rule values within a  rec type, with its type/status, review and exception axes, rule values and item-level detail.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The system-generated identifier for the rec result. Comprises the rec definition id, the instance id, the rec type and the core rule values. | 
**rec_type** | **str** | The type of rec that the result belongs to (e.g. Holding). Available values: Holding, CashHolding, Valuation, InputTransaction, OutputTransaction, SettlementActivity. | 
**instance_id** | [**RecInstanceId**](RecInstanceId.md) |  | 
**rec_definition_id** | [**ResourceId**](ResourceId.md) |  | 
**run_number** | **int** | The run number within the instance. Increments with each re-run. | 
**run_as_at** | **datetime** | The asAt datetime at which the run happened. | 
**dates_reconciled** | [**RecDatesReconciled**](RecDatesReconciled.md) |  | 
**result_type** | **str** | The type of result. Exceptions: PartialMatch, PartialCross, Break. Non-exceptions: Match, Cross. Available values: Match, Cross, PartialMatch, PartialCross, Break. | 
**result_cardinality** | **str** | The item cardinality of the result, read left to right (e.g. OneToOne, ManyToNone). Available values: OneToOne, OneToMany, ManyToOne, ManyToMany, OneToNone, ManyToNone, NoneToOne, NoneToMany, NoneToNone. | 
**result_life_cycle** | **str** | The run-over-run change in the result, evaluated each run against the prior run. Available values: New, Unchanged, Changed, Cleared. | 
**exception** | [**RecResultException**](RecResultException.md) |  | [optional] 
**review** | [**RecResultReview**](RecResultReview.md) |  | 
**core_rules** | [**List[CoreRuleValues]**](CoreRuleValues.md) | The core matching rules and the values that pin this result to its reconciled position. | 
**aggregate_rules** | [**List[AggregateRuleValues]**](AggregateRuleValues.md) | The aggregate matching rules and their measured values. | 
**supplemental_attributes** | [**List[SupplementalAttributeValues]**](SupplementalAttributeValues.md) | Additional attribute values carried on the result for context. Do not contribute to matching or the result id. | 
**items** | [**RecResultItemDetails**](RecResultItemDetails.md) |  | 
**comments** | [**List[RecUserComment]**](RecUserComment.md) | User-authored comments attached to the result. Carried forward across runs. | 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Properties in the RecResult domain. Filterable and sortable. | [optional] 
**assigned_user** | **str** | The LUSID user id assigned to the result. | [optional] 
**assigned_role** | **str** | The LUSID IAM role id assigned to the result. | [optional] 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.rec_result import RecResult
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: StrictStr = "example_id"
rec_type: StrictStr = "example_rec_type"
instance_id: RecInstanceId = # Replace with your value
rec_definition_id: ResourceId = # Replace with your value
run_number: StrictInt = # Replace with your value
run_number: StrictInt = 42
run_as_at: datetime = # Replace with your value
dates_reconciled: RecDatesReconciled = # Replace with your value
result_type: StrictStr = "example_result_type"
result_cardinality: StrictStr = "example_result_cardinality"
result_life_cycle: StrictStr = "example_result_life_cycle"
exception: Optional[RecResultException] = None
review: RecResultReview
core_rules: List[CoreRuleValues] = # Replace with your value
aggregate_rules: List[AggregateRuleValues] = # Replace with your value
supplemental_attributes: List[SupplementalAttributeValues] = # Replace with your value
items: RecResultItemDetails
comments: List[RecUserComment] = # Replace with your value
properties: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
assigned_user: Optional[StrictStr] = "example_assigned_user"
assigned_role: Optional[StrictStr] = "example_assigned_role"
href: Optional[StrictStr] = "example_href"
version: Optional[Version] = None
links: Optional[List[Link]] = None
rec_result_instance = RecResult(id=id, rec_type=rec_type, instance_id=instance_id, rec_definition_id=rec_definition_id, run_number=run_number, run_as_at=run_as_at, dates_reconciled=dates_reconciled, result_type=result_type, result_cardinality=result_cardinality, result_life_cycle=result_life_cycle, exception=exception, review=review, core_rules=core_rules, aggregate_rules=aggregate_rules, supplemental_attributes=supplemental_attributes, items=items, comments=comments, properties=properties, assigned_user=assigned_user, assigned_role=assigned_role, href=href, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

