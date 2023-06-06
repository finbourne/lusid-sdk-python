# DescribedAddressKey

An address key with additional data describing what this key is for.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_key** | **str** | Address key of some underlying object e.g. Valuation/PV, Instrument/Features | [optional] 
**description** | **str** | Description of the address key. | [optional] 

## Example

```python
from lusid.models.described_address_key import DescribedAddressKey

# TODO update the JSON string below
json = "{}"
# create an instance of DescribedAddressKey from a JSON string
described_address_key_instance = DescribedAddressKey.from_json(json)
# print the JSON string representation of the object
print DescribedAddressKey.to_json()

# convert the object into a dict
described_address_key_dict = described_address_key_instance.to_dict()
# create an instance of DescribedAddressKey from a dict
described_address_key_form_dict = described_address_key.from_dict(described_address_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


