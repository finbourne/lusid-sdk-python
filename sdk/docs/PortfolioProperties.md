# PortfolioProperties


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The portfolio properties. These will be from the &#39;Portfolio&#39; domain. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.portfolio_properties import PortfolioProperties

# TODO update the JSON string below
json = "{}"
# create an instance of PortfolioProperties from a JSON string
portfolio_properties_instance = PortfolioProperties.from_json(json)
# print the JSON string representation of the object
print PortfolioProperties.to_json()

# convert the object into a dict
portfolio_properties_dict = portfolio_properties_instance.to_dict()
# create an instance of PortfolioProperties from a dict
portfolio_properties_form_dict = portfolio_properties.from_dict(portfolio_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


