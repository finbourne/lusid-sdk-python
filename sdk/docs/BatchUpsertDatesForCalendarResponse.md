# BatchUpsertDatesForCalendarResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**Dict[str, CalendarDate]**](CalendarDate.md) | The dates which have been successfully upserted. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The dates that could not be upserted along with a reason for their failure. | [optional] 
**metadata** | **Dict[str, List[ResponseMetaData]]** | Contains warnings related to the upserted dates | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.batch_upsert_dates_for_calendar_response import BatchUpsertDatesForCalendarResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BatchUpsertDatesForCalendarResponse from a JSON string
batch_upsert_dates_for_calendar_response_instance = BatchUpsertDatesForCalendarResponse.from_json(json)
# print the JSON string representation of the object
print BatchUpsertDatesForCalendarResponse.to_json()

# convert the object into a dict
batch_upsert_dates_for_calendar_response_dict = batch_upsert_dates_for_calendar_response_instance.to_dict()
# create an instance of BatchUpsertDatesForCalendarResponse from a dict
batch_upsert_dates_for_calendar_response_form_dict = batch_upsert_dates_for_calendar_response.from_dict(batch_upsert_dates_for_calendar_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


