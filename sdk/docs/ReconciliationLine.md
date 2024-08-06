# ReconciliationLine

In evaluating a left and right hand side holding or valuation set, two data records result. These are then compared based on a set of  rules. This results in either a match or failure to match. If there is a match both left and right will be present, otherwise one will not.  A difference will be present if a match was calculated.  The options used in comparison may result in elision of results where an exact or tolerable match is made.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | **Dict[str, object]** | Left hand side of the comparison | [optional] 
**right** | **Dict[str, object]** | Right hand side of the comparison | [optional] 
**difference** | **Dict[str, object]** | Difference between LHS and RHS of comparison | [optional] 
**result_comparison** | **Dict[str, object]** | The logical or semantic description of the difference, e.g. \&quot;Matches\&quot; or \&quot;MatchesWithTolerance\&quot; or \&quot;Failed\&quot;. | [optional] 

## Example

```python
from lusid.models.reconciliation_line import ReconciliationLine

# TODO update the JSON string below
json = "{}"
# create an instance of ReconciliationLine from a JSON string
reconciliation_line_instance = ReconciliationLine.from_json(json)
# print the JSON string representation of the object
print ReconciliationLine.to_json()

# convert the object into a dict
reconciliation_line_dict = reconciliation_line_instance.to_dict()
# create an instance of ReconciliationLine from a dict
reconciliation_line_form_dict = reconciliation_line.from_dict(reconciliation_line_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


