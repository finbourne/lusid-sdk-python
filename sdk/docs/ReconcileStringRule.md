# ReconcileStringRule

Comparison of string values
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comparison_type** | **str** | The available values are: Exact, Contains, CaseInsensitive, ContainsAnyCase, IsOneOf, IsOneOfCaseInsensitive | 
**one_of_candidates** | **Dict[str, List[str]]** | For cases of \&quot;IsOneOf\&quot; or \&quot;IsOneOfCaseInsensitive\&quot;, a mapping from the left hand to side to lists of  equivalent alternative values on the right hand side.  Fuzzy matching of strings against one of a set. There can be cases where systems \&quot;A\&quot; and \&quot;B\&quot; might use different terms for the same logical entity. A common case would be  comparison of something like a day count fraction where some convention like the \&quot;actual 365\&quot; convention might be represented as one of [\&quot;A365\&quot;, \&quot;Act365\&quot;, \&quot;Actual365\&quot;] or similar.  This is to allow this kind of fuzzy matching of values. Note that as this is exhaustive comparison across sets it will be slow and should therefore be used sparingly. | [optional] 
**applies_to** | [**AggregateSpec**](AggregateSpec.md) |  | 
**rule_type** | **str** | The available values are: ReconcileNumericRule, ReconcileDateTimeRule, ReconcileStringRule, ReconcileExact | 
## Example

```python
from lusid.models.reconcile_string_rule import ReconcileStringRule
from typing import Any, Dict, List, Optional
from pydantic.v1 import Field, StrictStr, conlist, validator

comparison_type: StrictStr = "example_comparison_type"
one_of_candidates: Optional[Dict[str, conlist(StrictStr)]] = # Replace with your value
applies_to: AggregateSpec = # Replace with your value
rule_type: StrictStr = "example_rule_type"
reconcile_string_rule_instance = ReconcileStringRule(comparison_type=comparison_type, one_of_candidates=one_of_candidates, applies_to=applies_to, rule_type=rule_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

