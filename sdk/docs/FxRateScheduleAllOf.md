# FxRateScheduleAllOf


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
from lusid.models.fx_rate_schedule_all_of import FxRateScheduleAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of FxRateScheduleAllOf from a JSON string
fx_rate_schedule_all_of_instance = FxRateScheduleAllOf.from_json(json)
# print the JSON string representation of the object
print FxRateScheduleAllOf.to_json()

# convert the object into a dict
fx_rate_schedule_all_of_dict = fx_rate_schedule_all_of_instance.to_dict()
# create an instance of FxRateScheduleAllOf from a dict
fx_rate_schedule_all_of_form_dict = fx_rate_schedule_all_of.from_dict(fx_rate_schedule_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


