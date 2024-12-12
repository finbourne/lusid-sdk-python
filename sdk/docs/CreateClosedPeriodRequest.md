# CreateClosedPeriodRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**closed_period_id** | **str** | The unique Id of the Closed Period. The ClosedPeriodId, together with the Timeline Scope and Code, uniquely identifies a Closed Period | [optional] 
**effective_end** | **datetime** | The effective end of the Closed Period | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The Closed Periods properties. These will be from the &#39;ClosedPeriod&#39; domain. | [optional] 

## Example

```python
from lusid.models.create_closed_period_request import CreateClosedPeriodRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateClosedPeriodRequest from a JSON string
create_closed_period_request_instance = CreateClosedPeriodRequest.from_json(json)
# print the JSON string representation of the object
print CreateClosedPeriodRequest.to_json()

# convert the object into a dict
create_closed_period_request_dict = create_closed_period_request_instance.to_dict()
# create an instance of CreateClosedPeriodRequest from a dict
create_closed_period_request_form_dict = create_closed_period_request.from_dict(create_closed_period_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


