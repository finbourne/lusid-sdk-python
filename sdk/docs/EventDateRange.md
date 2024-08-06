# EventDateRange

A standard representation of the effective date range for the event, used for display, filtering and windowing use cases.  The start and end values for the eventDateRange are mapped from the particular dates contained within the specific  InstrumentEvent schema.  Note that the start and end values may be identical for some types of events.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **datetime** |  | [optional] 
**end** | **datetime** |  | [optional] 

## Example

```python
from lusid.models.event_date_range import EventDateRange

# TODO update the JSON string below
json = "{}"
# create an instance of EventDateRange from a JSON string
event_date_range_instance = EventDateRange.from_json(json)
# print the JSON string representation of the object
print EventDateRange.to_json()

# convert the object into a dict
event_date_range_dict = event_date_range_instance.to_dict()
# create an instance of EventDateRange from a dict
event_date_range_form_dict = event_date_range.from_dict(event_date_range_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


