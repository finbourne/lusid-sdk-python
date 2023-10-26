# BatchUpsertPortfolioTransactionsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**Dict[str, Transaction]**](Transaction.md) | The transactions which have been successfully upserted. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The transactions that could not be upserted along with a reason for their failure. | [optional] 
**metadata** | **Dict[str, List[ResponseMetaData]]** | Contains warnings related to unresolved instruments or non-existent transaction types for the upserted trades | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.batch_upsert_portfolio_transactions_response import BatchUpsertPortfolioTransactionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BatchUpsertPortfolioTransactionsResponse from a JSON string
batch_upsert_portfolio_transactions_response_instance = BatchUpsertPortfolioTransactionsResponse.from_json(json)
# print the JSON string representation of the object
print BatchUpsertPortfolioTransactionsResponse.to_json()

# convert the object into a dict
batch_upsert_portfolio_transactions_response_dict = batch_upsert_portfolio_transactions_response_instance.to_dict()
# create an instance of BatchUpsertPortfolioTransactionsResponse from a dict
batch_upsert_portfolio_transactions_response_form_dict = batch_upsert_portfolio_transactions_response.from_dict(batch_upsert_portfolio_transactions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


