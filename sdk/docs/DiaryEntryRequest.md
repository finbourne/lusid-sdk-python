# DiaryEntryRequest

The request to add a diary entry

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the diary entry. | [optional] 
**status** | **str** | The status of the diary entry. Defaults to &#39;Undefined&#39; and the allowed options are: &#39;Undefined&#39; and &#39;Estimate&#39;. | [optional] 
**effective_at** | **datetime** | The effective time of the diary entry. | 
**query_as_at** | **datetime** | The query time of the diary entry. Defaults to latest. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties for the diary entry. | [optional] 

## Example

```python
from lusid.models.diary_entry_request import DiaryEntryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DiaryEntryRequest from a JSON string
diary_entry_request_instance = DiaryEntryRequest.from_json(json)
# print the JSON string representation of the object
print DiaryEntryRequest.to_json()

# convert the object into a dict
diary_entry_request_dict = diary_entry_request_instance.to_dict()
# create an instance of DiaryEntryRequest from a dict
diary_entry_request_form_dict = diary_entry_request.from_dict(diary_entry_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


