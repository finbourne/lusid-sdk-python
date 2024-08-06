# PortfolioIdList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[ResourceId]**](ResourceId.md) |  | 
**reference_list_type** | **str** | The reference list values. The available values are: PortfolioGroupIdList, PortfolioIdList, AddressKeyList, StringList, InstrumentList, DecimalList, PropertyList | 

## Example

```python
from lusid.models.portfolio_id_list import PortfolioIdList

# TODO update the JSON string below
json = "{}"
# create an instance of PortfolioIdList from a JSON string
portfolio_id_list_instance = PortfolioIdList.from_json(json)
# print the JSON string representation of the object
print PortfolioIdList.to_json()

# convert the object into a dict
portfolio_id_list_dict = portfolio_id_list_instance.to_dict()
# create an instance of PortfolioIdList from a dict
portfolio_id_list_form_dict = portfolio_id_list.from_dict(portfolio_id_list_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


