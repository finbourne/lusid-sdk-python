# BookTransactionsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocation_ids** | [**List[ResourceId]**](ResourceId.md) | A collection of Allocation IDs | 
**transaction_properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | A collection of properties | [optional] 

## Example

```python
from lusid.models.book_transactions_request import BookTransactionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BookTransactionsRequest from a JSON string
book_transactions_request_instance = BookTransactionsRequest.from_json(json)
# print the JSON string representation of the object
print BookTransactionsRequest.to_json()

# convert the object into a dict
book_transactions_request_dict = book_transactions_request_instance.to_dict()
# create an instance of BookTransactionsRequest from a dict
book_transactions_request_form_dict = book_transactions_request.from_dict(book_transactions_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


