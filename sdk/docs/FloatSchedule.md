# FloatSchedule

Schedule for fixed coupon payments

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | Date to start generate from | [optional] 
**maturity_date** | **datetime** | Date to generate to | [optional] 
**flow_conventions** | [**FlowConventions**](FlowConventions.md) |  | [optional] 
**convention_name** | [**FlowConventionName**](FlowConventionName.md) |  | [optional] 
**index_convention_name** | [**FlowConventionName**](FlowConventionName.md) |  | [optional] 
**index_conventions** | [**IndexConvention**](IndexConvention.md) |  | [optional] 
**notional** | **float** | Scaling factor, the quantity outstanding on which the rate will be paid. | [optional] 
**payment_currency** | **str** | Payment currency. This does not have to be the same as the nominal bond or observation/reset currency. | [optional] 
**spread** | **float** | Spread over floating rate given as a fraction. | [optional] 
**stub_type** | **str** | StubType required of the schedule    Supported string (enumeration) values are: [ShortFront, ShortBack, LongBack, LongFront, Both]. | [optional] 
**schedule_type** | **str** | The available values are: Fixed, Float, Optionality, Step, Exercise, FxRate, Invalid | 

## Example

```python
from lusid.models.float_schedule import FloatSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of FloatSchedule from a JSON string
float_schedule_instance = FloatSchedule.from_json(json)
# print the JSON string representation of the object
print FloatSchedule.to_json()

# convert the object into a dict
float_schedule_dict = float_schedule_instance.to_dict()
# create an instance of FloatSchedule from a dict
float_schedule_form_dict = float_schedule.from_dict(float_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


