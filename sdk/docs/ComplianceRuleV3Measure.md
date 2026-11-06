# ComplianceRuleV3Measure

How a rule reduces its filtered (and optionally grouped) subject rows to the single number a check is  applied to: a metric field, the aggregate combining its values, and what it is expressed relative to.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric** | **str** |  | [optional] 
**aggregate** | **str** | Available values: Sum, Min, Max, Average, Count, CountDistinct, WeightedSum, SumAbsolute. | 
**denominator** | **str** | Available values: None, PortfolioValue, GrossValue, NetValue, FilteredSubsetTotal, GroupNav, GroupGrossExposure, GroupFilteredSubsetTotal. | [optional] 
**denominator_metric** | **str** |  | [optional] 
**weight_metric** | **str** |  | [optional] 
**denominator_property** | **str** |  | [optional] 
**filter** | [**ComplianceRuleV3FilterNode**](ComplianceRuleV3FilterNode.md) |  | [optional] 
## Example

```python
from lusid.models.compliance_rule_v3_measure import ComplianceRuleV3Measure
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

metric: Optional[StrictStr] = "example_metric"
aggregate: StrictStr = "example_aggregate"
denominator: Optional[StrictStr] = "example_denominator"
denominator_metric: Optional[StrictStr] = "example_denominator_metric"
weight_metric: Optional[StrictStr] = "example_weight_metric"
denominator_property: Optional[StrictStr] = "example_denominator_property"
filter: Optional[ComplianceRuleV3FilterNode] = None
compliance_rule_v3_measure_instance = ComplianceRuleV3Measure(metric=metric, aggregate=aggregate, denominator=denominator, denominator_metric=denominator_metric, weight_metric=weight_metric, denominator_property=denominator_property, filter=filter)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

