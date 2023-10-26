# StringList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | **List[str]** |  | 
**reference_list_type** | **str** | The reference list values. The available values are: PortfolioGroupIdList, PortfolioIdList, AddressKeyList, StringList, InstrumentList, DecimalList | 

## Example

```python
from lusid.models.string_list import StringList

# TODO update the JSON string below
json = "{}"
# create an instance of StringList from a JSON string
string_list_instance = StringList.from_json(json)
# print the JSON string representation of the object
print StringList.to_json()

# convert the object into a dict
string_list_dict = string_list_instance.to_dict()
# create an instance of StringList from a dict
string_list_form_dict = string_list.from_dict(string_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


