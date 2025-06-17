# ClosedPeriod


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**closed_period_id** | **str** | The unique Id of the Closed Period. The ClosedPeriodId, together with the Timeline Scope and Code, uniquely identifies a Closed Period | [optional] 
**effective_start** | **datetime** | The effective start of the Closed Period | [optional] 
**effective_end** | **datetime** | The effective end of the Closed Period | [optional] 
**as_at_closed** | **datetime** | The asAt closed datetime for the Closed Period | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The Closed Periods properties. These will be from the &#39;ClosedPeriod&#39; domain. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested asAt datetime. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.closed_period import ClosedPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of ClosedPeriod from a JSON string
closed_period_instance = ClosedPeriod.from_json(json)
# print the JSON string representation of the object
print ClosedPeriod.to_json()

# convert the object into a dict
closed_period_dict = closed_period_instance.to_dict()
# create an instance of ClosedPeriod from a dict
closed_period_form_dict = closed_period.from_dict(closed_period_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


