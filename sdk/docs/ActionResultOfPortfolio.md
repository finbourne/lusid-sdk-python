# ActionResultOfPortfolio


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **object** |  | [optional] 
**value** | [**Portfolio**](Portfolio.md) |  | [optional] 

## Example

```python
from lusid.models.action_result_of_portfolio import ActionResultOfPortfolio

# TODO update the JSON string below
json = "{}"
# create an instance of ActionResultOfPortfolio from a JSON string
action_result_of_portfolio_instance = ActionResultOfPortfolio.from_json(json)
# print the JSON string representation of the object
print ActionResultOfPortfolio.to_json()

# convert the object into a dict
action_result_of_portfolio_dict = action_result_of_portfolio_instance.to_dict()
# create an instance of ActionResultOfPortfolio from a dict
action_result_of_portfolio_form_dict = action_result_of_portfolio.from_dict(action_result_of_portfolio_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


