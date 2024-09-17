# FundIdList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[ResourceId]**](ResourceId.md) |  | 
**reference_list_type** | **str** | The reference list values. The available values are: PortfolioGroupIdList, PortfolioIdList, AddressKeyList, StringList, InstrumentList, DecimalList, PropertyList, FundIdList | 

## Example

```python
from lusid.models.fund_id_list import FundIdList

# TODO update the JSON string below
json = "{}"
# create an instance of FundIdList from a JSON string
fund_id_list_instance = FundIdList.from_json(json)
# print the JSON string representation of the object
print FundIdList.to_json()

# convert the object into a dict
fund_id_list_dict = fund_id_list_instance.to_dict()
# create an instance of FundIdList from a dict
fund_id_list_form_dict = fund_id_list.from_dict(fund_id_list_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


