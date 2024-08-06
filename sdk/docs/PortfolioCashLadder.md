# PortfolioCashLadder


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | The currency of the cash-flows. | 
**sub_holding_keys** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | The sub-holding properties which identify the holding. Each property will be from the &#39;Transaction&#39; domain. These are configured on a transaction portfolio. | [optional] 
**records** | [**List[CashLadderRecord]**](CashLadderRecord.md) | A record of cash flows on a specific date. | 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The records that could not be returned along with a reason for their failure. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.portfolio_cash_ladder import PortfolioCashLadder

# TODO update the JSON string below
json = "{}"
# create an instance of PortfolioCashLadder from a JSON string
portfolio_cash_ladder_instance = PortfolioCashLadder.from_json(json)
# print the JSON string representation of the object
print PortfolioCashLadder.to_json()

# convert the object into a dict
portfolio_cash_ladder_dict = portfolio_cash_ladder_instance.to_dict()
# create an instance of PortfolioCashLadder from a dict
portfolio_cash_ladder_form_dict = portfolio_cash_ladder.from_dict(portfolio_cash_ladder_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


