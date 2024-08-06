# PortfolioReturnBreakdown

A list of Composite Breakdowns.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**rate_of_return** | **float** | The return number. | [optional] 
**opening_market_value** | **float** | The opening market value. | [optional] 
**closing_market_value** | **float** | The closing market value. | [optional] 
**weight** | **float** | The weight of the constituent into the composite. | [optional] 
**constituents_in_the_composite** | **int** | The number of members in the Composite on the given day. | [optional] 
**constituents_missing** | **int** | The number of the constituents which have a missing return on that day. | [optional] 
**currency** | **str** | The currency of the portfolio. | [optional] 
**open_fx_rate** | **float** | The opening fxRate which is used in calculation. | [optional] 
**close_fx_rate** | **float** | The closing fxRate which is used in calculation. | [optional] 
**local_rate_of_return** | **float** | The rate of return in the local currency. | [optional] 
**local_opening_market_value** | **float** | The opening market value in the local currency. | [optional] 
**local_closing_market_value** | **float** | The closing market value in the local currency. | [optional] 

## Example

```python
from lusid.models.portfolio_return_breakdown import PortfolioReturnBreakdown

# TODO update the JSON string below
json = "{}"
# create an instance of PortfolioReturnBreakdown from a JSON string
portfolio_return_breakdown_instance = PortfolioReturnBreakdown.from_json(json)
# print the JSON string representation of the object
print PortfolioReturnBreakdown.to_json()

# convert the object into a dict
portfolio_return_breakdown_dict = portfolio_return_breakdown_instance.to_dict()
# create an instance of PortfolioReturnBreakdown from a dict
portfolio_return_breakdown_form_dict = portfolio_return_breakdown.from_dict(portfolio_return_breakdown_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


