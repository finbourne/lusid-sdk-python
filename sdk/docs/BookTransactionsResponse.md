# BookTransactionsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**Dict[str, Transaction]**](Transaction.md) |  | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) |  | [optional] 

## Example

```python
from lusid.models.book_transactions_response import BookTransactionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BookTransactionsResponse from a JSON string
book_transactions_response_instance = BookTransactionsResponse.from_json(json)
# print the JSON string representation of the object
print BookTransactionsResponse.to_json()

# convert the object into a dict
book_transactions_response_dict = book_transactions_response_instance.to_dict()
# create an instance of BookTransactionsResponse from a dict
book_transactions_response_form_dict = book_transactions_response.from_dict(book_transactions_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


