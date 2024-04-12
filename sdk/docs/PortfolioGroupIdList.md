# PortfolioGroupIdList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[ResourceId]**](ResourceId.md) |  | 
**reference_list_type** | **str** | The reference list values. The available values are: PortfolioGroupIdList, PortfolioIdList, AddressKeyList, StringList, InstrumentList, DecimalList, PropertyList | 

## Example

```python
from lusid.models.portfolio_group_id_list import PortfolioGroupIdList

# TODO update the JSON string below
json = "{}"
# create an instance of PortfolioGroupIdList from a JSON string
portfolio_group_id_list_instance = PortfolioGroupIdList.from_json(json)
# print the JSON string representation of the object
print PortfolioGroupIdList.to_json()

# convert the object into a dict
portfolio_group_id_list_dict = portfolio_group_id_list_instance.to_dict()
# create an instance of PortfolioGroupIdList from a dict
portfolio_group_id_list_form_dict = portfolio_group_id_list.from_dict(portfolio_group_id_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


