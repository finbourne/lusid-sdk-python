# ClosePeriodDiaryEntryRequest

A definition for the period you wish to close

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diary_entry_code** | **str** | Unique code assigned to a period. When left blank a code will be created by the system in the format &#39;yyyyMMDD&#39;. | [optional] 
**name** | **str** | Identifiable Name assigned to the period. Where left blank, the system will generate a name in the format &#39;yyyyMMDD&#39;. | [optional] 
**effective_at** | **datetime** | The effective time of the diary entry. | [optional] 
**query_as_at** | **datetime** | The query time of the diary entry. Defaults to latest. | [optional] 
**status** | **str** | The status of the diary entry. Defaults to &#39;Undefined&#39; for valuation points and &#39;Estimate&#39; for closing periods. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties for the diary entry. | [optional] 

## Example

```python
from lusid.models.close_period_diary_entry_request import ClosePeriodDiaryEntryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClosePeriodDiaryEntryRequest from a JSON string
close_period_diary_entry_request_instance = ClosePeriodDiaryEntryRequest.from_json(json)
# print the JSON string representation of the object
print ClosePeriodDiaryEntryRequest.to_json()

# convert the object into a dict
close_period_diary_entry_request_dict = close_period_diary_entry_request_instance.to_dict()
# create an instance of ClosePeriodDiaryEntryRequest from a dict
close_period_diary_entry_request_form_dict = close_period_diary_entry_request.from_dict(close_period_diary_entry_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


