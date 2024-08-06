# UpdatePortfolioGroupRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the portfolio group. | 
**description** | **str** | A long form description of the portfolio group. | [optional] 

## Example

```python
from lusid.models.update_portfolio_group_request import UpdatePortfolioGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePortfolioGroupRequest from a JSON string
update_portfolio_group_request_instance = UpdatePortfolioGroupRequest.from_json(json)
# print the JSON string representation of the object
print UpdatePortfolioGroupRequest.to_json()

# convert the object into a dict
update_portfolio_group_request_dict = update_portfolio_group_request_instance.to_dict()
# create an instance of UpdatePortfolioGroupRequest from a dict
update_portfolio_group_request_form_dict = update_portfolio_group_request.from_dict(update_portfolio_group_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


