# UpdatePortfolioRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the transaction portfolio. | 
**description** | **str** | The description of the transaction portfolio. | [optional] 

## Example

```python
from lusid.models.update_portfolio_request import UpdatePortfolioRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePortfolioRequest from a JSON string
update_portfolio_request_instance = UpdatePortfolioRequest.from_json(json)
# print the JSON string representation of the object
print UpdatePortfolioRequest.to_json()

# convert the object into a dict
update_portfolio_request_dict = update_portfolio_request_instance.to_dict()
# create an instance of UpdatePortfolioRequest from a dict
update_portfolio_request_form_dict = update_portfolio_request.from_dict(update_portfolio_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


