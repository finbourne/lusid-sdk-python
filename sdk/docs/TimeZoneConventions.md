# TimeZoneConventions

Provides information on the primary time zone of an instrument and optional cut labels  for defining times to be used by instrument events.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_time_zone** | **str** | The IANA time zone code for the instrument. | 
**start_of_day** | **str** | A LUSID Cut Label code used for generating instrument events at a time other than local midnight. | [optional] 
**primary_market_open** | **str** | A LUSID Cut Label code used for delaying the transaction time of certain instrument events until market open. | [optional] 

## Example

```python
from lusid.models.time_zone_conventions import TimeZoneConventions

# TODO update the JSON string below
json = "{}"
# create an instance of TimeZoneConventions from a JSON string
time_zone_conventions_instance = TimeZoneConventions.from_json(json)
# print the JSON string representation of the object
print TimeZoneConventions.to_json()

# convert the object into a dict
time_zone_conventions_dict = time_zone_conventions_instance.to_dict()
# create an instance of TimeZoneConventions from a dict
time_zone_conventions_form_dict = time_zone_conventions.from_dict(time_zone_conventions_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


