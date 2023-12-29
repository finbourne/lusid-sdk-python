# DiaryEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**abor_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**diary_entry_code** | **str** | The code of the diary entry. | [optional] 
**type** | **str** | The type of the diary entry. | 
**name** | **str** | The name of the diary entry. | [optional] 
**status** | **str** | The status of the diary entry. Defaults to &#39;Undefined&#39; for valuation points and &#39;Estimate&#39; for closing periods. | 
**effective_at** | **datetime** | The effective time of the diary entry. | 
**query_as_at** | **datetime** | The query time of the diary entry. Defaults to latest. | [optional] 
**previous_entry_time** | **datetime** | The entry time of the previous diary entry. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties for the diary entry. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.diary_entry import DiaryEntry

# TODO update the JSON string below
json = "{}"
# create an instance of DiaryEntry from a JSON string
diary_entry_instance = DiaryEntry.from_json(json)
# print the JSON string representation of the object
print DiaryEntry.to_json()

# convert the object into a dict
diary_entry_dict = diary_entry_instance.to_dict()
# create an instance of DiaryEntry from a dict
diary_entry_form_dict = diary_entry.from_dict(diary_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


