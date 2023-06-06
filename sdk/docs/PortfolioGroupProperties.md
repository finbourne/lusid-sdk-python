# PortfolioGroupProperties


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The portfolio group properties. These will be from the &#39;PortfolioGroup&#39; domain. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.portfolio_group_properties import PortfolioGroupProperties

# TODO update the JSON string below
json = "{}"
# create an instance of PortfolioGroupProperties from a JSON string
portfolio_group_properties_instance = PortfolioGroupProperties.from_json(json)
# print the JSON string representation of the object
print PortfolioGroupProperties.to_json()

# convert the object into a dict
portfolio_group_properties_dict = portfolio_group_properties_instance.to_dict()
# create an instance of PortfolioGroupProperties from a dict
portfolio_group_properties_form_dict = portfolio_group_properties.from_dict(portfolio_group_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


