# UpsertPortfolioTransactionsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**Version**](Version.md) |  | 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**metadata** | **Dict[str, List[ResponseMetaData]]** | Contains warnings related to unresolved instruments or non-existent transaction types for the upserted trades | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.upsert_portfolio_transactions_response import UpsertPortfolioTransactionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertPortfolioTransactionsResponse from a JSON string
upsert_portfolio_transactions_response_instance = UpsertPortfolioTransactionsResponse.from_json(json)
# print the JSON string representation of the object
print UpsertPortfolioTransactionsResponse.to_json()

# convert the object into a dict
upsert_portfolio_transactions_response_dict = upsert_portfolio_transactions_response_instance.to_dict()
# create an instance of UpsertPortfolioTransactionsResponse from a dict
upsert_portfolio_transactions_response_form_dict = upsert_portfolio_transactions_response.from_dict(upsert_portfolio_transactions_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


