# VersionedResourceListWithWarningsOfPortfolioHolding


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**Version**](Version.md) |  | 
**values** | [**List[PortfolioHolding]**](PortfolioHolding.md) | The resources to list. | 
**href** | **str** | The URI of the resource list. | [optional] 
**next_page** | **str** | The next page of results. | [optional] 
**previous_page** | **str** | The previous page of results. | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.versioned_resource_list_with_warnings_of_portfolio_holding import VersionedResourceListWithWarningsOfPortfolioHolding

# TODO update the JSON string below
json = "{}"
# create an instance of VersionedResourceListWithWarningsOfPortfolioHolding from a JSON string
versioned_resource_list_with_warnings_of_portfolio_holding_instance = VersionedResourceListWithWarningsOfPortfolioHolding.from_json(json)
# print the JSON string representation of the object
print VersionedResourceListWithWarningsOfPortfolioHolding.to_json()

# convert the object into a dict
versioned_resource_list_with_warnings_of_portfolio_holding_dict = versioned_resource_list_with_warnings_of_portfolio_holding_instance.to_dict()
# create an instance of VersionedResourceListWithWarningsOfPortfolioHolding from a dict
versioned_resource_list_with_warnings_of_portfolio_holding_form_dict = versioned_resource_list_with_warnings_of_portfolio_holding.from_dict(versioned_resource_list_with_warnings_of_portfolio_holding_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


