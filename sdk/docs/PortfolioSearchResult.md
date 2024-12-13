# PortfolioSearchResult

A list of portfolios.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**type** | **str** | The type of the portfolio. The available values are: Transaction, Reference, DerivedTransaction, SimplePosition | 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**description** | **str** | The long form description of the portfolio. | [optional] 
**display_name** | **str** | The name of the portfolio. | 
**is_derived** | **bool** | Whether or not this is a derived portfolio. | [optional] [readonly] 
**created** | **datetime** | The effective datetime at which the portfolio was created. No transactions or constituents can be added to the portfolio before this date. | 
**parent_portfolio_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**base_currency** | **str** | The base currency of the portfolio. | [optional] 
**properties** | [**List[ModelProperty]**](ModelProperty.md) | The requested portfolio properties. These will be from the &#39;Portfolio&#39; domain. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.portfolio_search_result import PortfolioSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of PortfolioSearchResult from a JSON string
portfolio_search_result_instance = PortfolioSearchResult.from_json(json)
# print the JSON string representation of the object
print PortfolioSearchResult.to_json()

# convert the object into a dict
portfolio_search_result_dict = portfolio_search_result_instance.to_dict()
# create an instance of PortfolioSearchResult from a dict
portfolio_search_result_form_dict = portfolio_search_result.from_dict(portfolio_search_result_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


