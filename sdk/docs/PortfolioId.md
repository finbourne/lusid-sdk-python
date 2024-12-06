# PortfolioId


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | [**DataScope**](DataScope.md) |  | [optional] 
**identifier** | **str** |  | [optional] 

## Example

```python
from lusid.models.portfolio_id import PortfolioId

# TODO update the JSON string below
json = "{}"
# create an instance of PortfolioId from a JSON string
portfolio_id_instance = PortfolioId.from_json(json)
# print the JSON string representation of the object
print PortfolioId.to_json()

# convert the object into a dict
portfolio_id_dict = portfolio_id_instance.to_dict()
# create an instance of PortfolioId from a dict
portfolio_id_form_dict = portfolio_id.from_dict(portfolio_id_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


