# AddBusinessDaysToDateResponse

The date that is the requested number of business days after the given start date

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **datetime** |  | 

## Example

```python
from lusid.models.add_business_days_to_date_response import AddBusinessDaysToDateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddBusinessDaysToDateResponse from a JSON string
add_business_days_to_date_response_instance = AddBusinessDaysToDateResponse.from_json(json)
# print the JSON string representation of the object
print AddBusinessDaysToDateResponse.to_json()

# convert the object into a dict
add_business_days_to_date_response_dict = add_business_days_to_date_response_instance.to_dict()
# create an instance of AddBusinessDaysToDateResponse from a dict
add_business_days_to_date_response_form_dict = add_business_days_to_date_response.from_dict(add_business_days_to_date_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


