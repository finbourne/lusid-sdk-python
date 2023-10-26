# ReferenceList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_list_type** | **str** | The reference list values. The available values are: PortfolioGroupIdList, PortfolioIdList, AddressKeyList, StringList, InstrumentList, DecimalList | 

## Example

```python
from lusid.models.reference_list import ReferenceList

# TODO update the JSON string below
json = "{}"
# create an instance of ReferenceList from a JSON string
reference_list_instance = ReferenceList.from_json(json)
# print the JSON string representation of the object
print ReferenceList.to_json()

# convert the object into a dict
reference_list_dict = reference_list_instance.to_dict()
# create an instance of ReferenceList from a dict
reference_list_form_dict = reference_list.from_dict(reference_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


