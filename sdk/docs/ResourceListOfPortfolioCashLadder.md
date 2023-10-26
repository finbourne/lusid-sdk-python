# ResourceListOfPortfolioCashLadder


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[PortfolioCashLadder]**](PortfolioCashLadder.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_portfolio_cash_ladder import ResourceListOfPortfolioCashLadder

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfPortfolioCashLadder from a JSON string
resource_list_of_portfolio_cash_ladder_instance = ResourceListOfPortfolioCashLadder.from_json(json)
# print the JSON string representation of the object
print ResourceListOfPortfolioCashLadder.to_json()

# convert the object into a dict
resource_list_of_portfolio_cash_ladder_dict = resource_list_of_portfolio_cash_ladder_instance.to_dict()
# create an instance of ResourceListOfPortfolioCashLadder from a dict
resource_list_of_portfolio_cash_ladder_form_dict = resource_list_of_portfolio_cash_ladder.from_dict(resource_list_of_portfolio_cash_ladder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


