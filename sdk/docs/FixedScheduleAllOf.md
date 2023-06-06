# FixedScheduleAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | Date to start generate from | 
**maturity_date** | **datetime** | Date to generate to | 
**flow_conventions** | [**FlowConventions**](FlowConventions.md) |  | [optional] 
**coupon_rate** | **float** | Coupon rate given as a fraction. | [optional] 
**convention_name** | [**FlowConventionName**](FlowConventionName.md) |  | [optional] 
**notional** | **float** | Scaling factor, the quantity outstanding on which the rate will be paid. | [optional] 
**payment_currency** | **str** | Payment currency. This does not have to be the same as the nominal bond or observation/reset currency. | [optional] 
**stub_type** | **str** | StubType required of the schedule    Supported string (enumeration) values are: [ShortFront, ShortBack, LongBack, LongFront, Both]. | [optional] 
**schedule_type** | **str** | The available values are: Fixed, Float, Optionality, Step, Exercise, FxRate, Invalid | 

## Example

```python
from lusid.models.fixed_schedule_all_of import FixedScheduleAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of FixedScheduleAllOf from a JSON string
fixed_schedule_all_of_instance = FixedScheduleAllOf.from_json(json)
# print the JSON string representation of the object
print FixedScheduleAllOf.to_json()

# convert the object into a dict
fixed_schedule_all_of_dict = fixed_schedule_all_of_instance.to_dict()
# create an instance of FixedScheduleAllOf from a dict
fixed_schedule_all_of_form_dict = fixed_schedule_all_of.from_dict(fixed_schedule_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


