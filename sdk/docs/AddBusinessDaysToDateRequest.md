# AddBusinessDaysToDateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_day_offset** | **int** |  | 
**holiday_codes** | **List[str]** |  | 
**start_date** | **datetime** |  | [optional] 
**as_at** | **datetime** |  | [optional] 

## Example

```python
from lusid.models.add_business_days_to_date_request import AddBusinessDaysToDateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddBusinessDaysToDateRequest from a JSON string
add_business_days_to_date_request_instance = AddBusinessDaysToDateRequest.from_json(json)
# print the JSON string representation of the object
print AddBusinessDaysToDateRequest.to_json()

# convert the object into a dict
add_business_days_to_date_request_dict = add_business_days_to_date_request_instance.to_dict()
# create an instance of AddBusinessDaysToDateRequest from a dict
add_business_days_to_date_request_form_dict = add_business_days_to_date_request.from_dict(add_business_days_to_date_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


