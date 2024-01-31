# RelativeDateOffset

Defines a date offset which is relative to some anchor date.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days** | **int** | The number of business days to add to the anchor date. | 
**business_day_convention** | **str** | The adjustment type to apply to dates that fall upon a non-business day, e.g. modified following or following.    Supported string (enumeration) values are: [NoAdjustment, Previous, P, Following, F, ModifiedPrevious, MP, ModifiedFollowing, MF, HalfMonthModifiedFollowing, Nearest]. | 

## Example

```python
from lusid.models.relative_date_offset import RelativeDateOffset

# TODO update the JSON string below
json = "{}"
# create an instance of RelativeDateOffset from a JSON string
relative_date_offset_instance = RelativeDateOffset.from_json(json)
# print the JSON string representation of the object
print RelativeDateOffset.to_json()

# convert the object into a dict
relative_date_offset_dict = relative_date_offset_instance.to_dict()
# create an instance of RelativeDateOffset from a dict
relative_date_offset_form_dict = relative_date_offset.from_dict(relative_date_offset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


