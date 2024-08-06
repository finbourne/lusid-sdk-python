# PortfolioEntityId

Specification of a portfolio or portfolio group id, its scope and which it is.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The scope within which the portfolio or portfolio group lives. | 
**code** | **str** | Portfolio name or code. | 
**portfolio_entity_type** | **str** | String identifier for portfolio e.g. \&quot;SinglePortfolio\&quot; and \&quot;GroupPortfolio\&quot;. If not specified, it is assumed to be a single portfolio. | [optional] 

## Example

```python
from lusid.models.portfolio_entity_id import PortfolioEntityId

# TODO update the JSON string below
json = "{}"
# create an instance of PortfolioEntityId from a JSON string
portfolio_entity_id_instance = PortfolioEntityId.from_json(json)
# print the JSON string representation of the object
print PortfolioEntityId.to_json()

# convert the object into a dict
portfolio_entity_id_dict = portfolio_entity_id_instance.to_dict()
# create an instance of PortfolioEntityId from a dict
portfolio_entity_id_form_dict = portfolio_entity_id.from_dict(portfolio_entity_id_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


