# FxRateSchedule

Schedule to define fx conversion of cashflows on complex bonds. If an fx schedule is defined then  on payment schedule generation the coupon and principal payoffs will be wrapped in an fx rate payoff method.  Either the fx rate is predefined (fixed) or relies on fx resets (floating).  Used in representation of dual currency bond.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fixing_lag** | **int** | If rate is not known upfront then will need a fixing rate. Can be fixed x number of days before payment date. | [optional] 
**fx_conversion_types** | **List[str]** | List of flags to indicate if coupon payments, principal payments or both are converted | [optional] 
**rate** | **float** | FxRate used to convert payments. Assumed to be in units of the ToCurrency so conversion is paymentAmount x fxRate | [optional] 
**to_currency** | **str** | Currency that payments are converted to | [optional] 
**schedule_type** | **str** | The available values are: Fixed, Float, Optionality, Step, Exercise, FxRate, Invalid | 

## Example

```python
from lusid.models.fx_rate_schedule import FxRateSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of FxRateSchedule from a JSON string
fx_rate_schedule_instance = FxRateSchedule.from_json(json)
# print the JSON string representation of the object
print FxRateSchedule.to_json()

# convert the object into a dict
fx_rate_schedule_dict = fx_rate_schedule_instance.to_dict()
# create an instance of FxRateSchedule from a dict
fx_rate_schedule_form_dict = fx_rate_schedule.from_dict(fx_rate_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


