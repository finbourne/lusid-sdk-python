# VersionedResourceListOfPortfolioHolding


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**Version**](Version.md) |  | 
**values** | [**List[PortfolioHolding]**](PortfolioHolding.md) |  | 
**href** | **str** |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.versioned_resource_list_of_portfolio_holding import VersionedResourceListOfPortfolioHolding

# TODO update the JSON string below
json = "{}"
# create an instance of VersionedResourceListOfPortfolioHolding from a JSON string
versioned_resource_list_of_portfolio_holding_instance = VersionedResourceListOfPortfolioHolding.from_json(json)
# print the JSON string representation of the object
print VersionedResourceListOfPortfolioHolding.to_json()

# convert the object into a dict
versioned_resource_list_of_portfolio_holding_dict = versioned_resource_list_of_portfolio_holding_instance.to_dict()
# create an instance of VersionedResourceListOfPortfolioHolding from a dict
versioned_resource_list_of_portfolio_holding_form_dict = versioned_resource_list_of_portfolio_holding.from_dict(versioned_resource_list_of_portfolio_holding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


