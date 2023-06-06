# IsBusinessDayResponse

Whether or not a DateTimeOffset is a business DateTime

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requested_date_time** | **datetime** |  | 
**is_business_day** | **bool** |  | 

## Example

```python
from lusid.models.is_business_day_response import IsBusinessDayResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IsBusinessDayResponse from a JSON string
is_business_day_response_instance = IsBusinessDayResponse.from_json(json)
# print the JSON string representation of the object
print IsBusinessDayResponse.to_json()

# convert the object into a dict
is_business_day_response_dict = is_business_day_response_instance.to_dict()
# create an instance of IsBusinessDayResponse from a dict
is_business_day_response_form_dict = is_business_day_response.from_dict(is_business_day_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


