# RecommendedSortBy


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_name** | **str** | The property key, identifier type, or field to be sorted by. | 
**sort_order** | **str** | The sorting direction. Either ascending (ASC) or descending (DESC). | [optional] 

## Example

```python
from lusid.models.recommended_sort_by import RecommendedSortBy

# TODO update the JSON string below
json = "{}"
# create an instance of RecommendedSortBy from a JSON string
recommended_sort_by_instance = RecommendedSortBy.from_json(json)
# print the JSON string representation of the object
print RecommendedSortBy.to_json()

# convert the object into a dict
recommended_sort_by_dict = recommended_sort_by_instance.to_dict()
# create an instance of RecommendedSortBy from a dict
recommended_sort_by_form_dict = recommended_sort_by.from_dict(recommended_sort_by_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


