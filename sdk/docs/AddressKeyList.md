# AddressKeyList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | **List[str]** |  | 
**reference_list_type** | **str** | The reference list values. The available values are: PortfolioGroupIdList, PortfolioIdList, AddressKeyList, StringList, InstrumentList, DecimalList, PropertyList | 

## Example

```python
from lusid.models.address_key_list import AddressKeyList

# TODO update the JSON string below
json = "{}"
# create an instance of AddressKeyList from a JSON string
address_key_list_instance = AddressKeyList.from_json(json)
# print the JSON string representation of the object
print AddressKeyList.to_json()

# convert the object into a dict
address_key_list_dict = address_key_list_instance.to_dict()
# create an instance of AddressKeyList from a dict
address_key_list_form_dict = address_key_list.from_dict(address_key_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


