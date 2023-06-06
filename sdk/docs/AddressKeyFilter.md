# AddressKeyFilter

Class specifying a filtering operation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | **str** | Address for the value in the row | [optional] 
**operator** | **str** | What sort of comparison is the filter performing. Can be either \&quot;eq\&quot; for equals or \&quot;neq\&quot; for not equals. | [optional] 
**right** | [**ResultValue**](ResultValue.md) |  | [optional] 

## Example

```python
from lusid.models.address_key_filter import AddressKeyFilter

# TODO update the JSON string below
json = "{}"
# create an instance of AddressKeyFilter from a JSON string
address_key_filter_instance = AddressKeyFilter.from_json(json)
# print the JSON string representation of the object
print AddressKeyFilter.to_json()

# convert the object into a dict
address_key_filter_dict = address_key_filter_instance.to_dict()
# create an instance of AddressKeyFilter from a dict
address_key_filter_form_dict = address_key_filter.from_dict(address_key_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


