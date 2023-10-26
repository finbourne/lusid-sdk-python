# GroupedResultOfAddressKey

Holder class for a group of results. It consists of a list of columns and values for that column.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | **List[str]** | The columns, or keys, for a particular group of results | [optional] 
**values** | [**List[ResultValue]**](ResultValue.md) | The values for the list of results | [optional] 

## Example

```python
from lusid.models.grouped_result_of_address_key import GroupedResultOfAddressKey

# TODO update the JSON string below
json = "{}"
# create an instance of GroupedResultOfAddressKey from a JSON string
grouped_result_of_address_key_instance = GroupedResultOfAddressKey.from_json(json)
# print the JSON string representation of the object
print GroupedResultOfAddressKey.to_json()

# convert the object into a dict
grouped_result_of_address_key_dict = grouped_result_of_address_key_instance.to_dict()
# create an instance of GroupedResultOfAddressKey from a dict
grouped_result_of_address_key_form_dict = grouped_result_of_address_key.from_dict(grouped_result_of_address_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


