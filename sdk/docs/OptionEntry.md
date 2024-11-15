# OptionEntry

Strike price against par and associated date for a bond call.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strike** | **float** | The strike on this date | 
**var_date** | **datetime** | The date at which the option can be actioned at this strike | 
**end_date** | **datetime** | If American exercise, this is the end of the exercise period.  Optional field. Defaults to the Date field if not set. | [optional] 

## Example

```python
from lusid.models.option_entry import OptionEntry

# TODO update the JSON string below
json = "{}"
# create an instance of OptionEntry from a JSON string
option_entry_instance = OptionEntry.from_json(json)
# print the JSON string representation of the object
print OptionEntry.to_json()

# convert the object into a dict
option_entry_dict = option_entry_instance.to_dict()
# create an instance of OptionEntry from a dict
option_entry_form_dict = option_entry.from_dict(option_entry_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


