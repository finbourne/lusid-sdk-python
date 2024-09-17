# PropertyList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[ModelProperty]**](ModelProperty.md) |  | 
**reference_list_type** | **str** | The reference list values. The available values are: PortfolioGroupIdList, PortfolioIdList, AddressKeyList, StringList, InstrumentList, DecimalList, PropertyList, FundIdList | 

## Example

```python
from lusid.models.property_list import PropertyList

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyList from a JSON string
property_list_instance = PropertyList.from_json(json)
# print the JSON string representation of the object
print PropertyList.to_json()

# convert the object into a dict
property_list_dict = property_list_instance.to_dict()
# create an instance of PropertyList from a dict
property_list_form_dict = property_list.from_dict(property_list_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


