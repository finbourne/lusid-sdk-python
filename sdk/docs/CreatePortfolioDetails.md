# CreatePortfolioDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**corporate_action_source_id** | [**ResourceId**](ResourceId.md) |  | [optional] 

## Example

```python
from lusid.models.create_portfolio_details import CreatePortfolioDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePortfolioDetails from a JSON string
create_portfolio_details_instance = CreatePortfolioDetails.from_json(json)
# print the JSON string representation of the object
print CreatePortfolioDetails.to_json()

# convert the object into a dict
create_portfolio_details_dict = create_portfolio_details_instance.to_dict()
# create an instance of CreatePortfolioDetails from a dict
create_portfolio_details_form_dict = create_portfolio_details.from_dict(create_portfolio_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


