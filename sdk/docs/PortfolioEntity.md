# PortfolioEntity

A list of portfolios.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | 
**entity_unique_id** | **str** | The unique id of the entity | 
**status** | **str** | The status of the entity at the current time | 
**prevailing_portfolio** | [**PortfolioWithoutHref**](PortfolioWithoutHref.md) |  | [optional] 
**deleted_portfolio** | [**PortfolioWithoutHref**](PortfolioWithoutHref.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.portfolio_entity import PortfolioEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PortfolioEntity from a JSON string
portfolio_entity_instance = PortfolioEntity.from_json(json)
# print the JSON string representation of the object
print PortfolioEntity.to_json()

# convert the object into a dict
portfolio_entity_dict = portfolio_entity_instance.to_dict()
# create an instance of PortfolioEntity from a dict
portfolio_entity_form_dict = portfolio_entity.from_dict(portfolio_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


