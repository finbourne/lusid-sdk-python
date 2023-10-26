# InstrumentList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | **List[str]** |  | 
**reference_list_type** | **str** | The reference list values. The available values are: PortfolioGroupIdList, PortfolioIdList, AddressKeyList, StringList, InstrumentList, DecimalList | 

## Example

```python
from lusid.models.instrument_list import InstrumentList

# TODO update the JSON string below
json = "{}"
# create an instance of InstrumentList from a JSON string
instrument_list_instance = InstrumentList.from_json(json)
# print the JSON string representation of the object
print InstrumentList.to_json()

# convert the object into a dict
instrument_list_dict = instrument_list_instance.to_dict()
# create an instance of InstrumentList from a dict
instrument_list_form_dict = instrument_list.from_dict(instrument_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


