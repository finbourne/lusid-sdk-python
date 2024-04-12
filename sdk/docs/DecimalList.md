# DecimalList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | **List[float]** |  | 
**reference_list_type** | **str** | The reference list values. The available values are: PortfolioGroupIdList, PortfolioIdList, AddressKeyList, StringList, InstrumentList, DecimalList, PropertyList | 

## Example

```python
from lusid.models.decimal_list import DecimalList

# TODO update the JSON string below
json = "{}"
# create an instance of DecimalList from a JSON string
decimal_list_instance = DecimalList.from_json(json)
# print the JSON string representation of the object
print DecimalList.to_json()

# convert the object into a dict
decimal_list_dict = decimal_list_instance.to_dict()
# create an instance of DecimalList from a dict
decimal_list_form_dict = decimal_list.from_dict(decimal_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


