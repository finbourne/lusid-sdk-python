# CompositeBreakdown

A list of Composite Breakdowns.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_at** | **datetime** | The effectiveAt for the calculation. | 
**composite** | [**PortfolioReturnBreakdown**](PortfolioReturnBreakdown.md) |  | [optional] 
**constituents** | [**List[PortfolioReturnBreakdown]**](PortfolioReturnBreakdown.md) | The constituents with their information which are part of the composite. | [optional] 

## Example

```python
from lusid.models.composite_breakdown import CompositeBreakdown

# TODO update the JSON string below
json = "{}"
# create an instance of CompositeBreakdown from a JSON string
composite_breakdown_instance = CompositeBreakdown.from_json(json)
# print the JSON string representation of the object
print CompositeBreakdown.to_json()

# convert the object into a dict
composite_breakdown_dict = composite_breakdown_instance.to_dict()
# create an instance of CompositeBreakdown from a dict
composite_breakdown_form_dict = composite_breakdown.from_dict(composite_breakdown_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


