# UpsertPortfolioGroupAccessMetadataRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**List[AccessMetadataValue]**](AccessMetadataValue.md) | The access control metadata to assign to portfolio groups that match the identifier | 

## Example

```python
from lusid.models.upsert_portfolio_group_access_metadata_request import UpsertPortfolioGroupAccessMetadataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertPortfolioGroupAccessMetadataRequest from a JSON string
upsert_portfolio_group_access_metadata_request_instance = UpsertPortfolioGroupAccessMetadataRequest.from_json(json)
# print the JSON string representation of the object
print UpsertPortfolioGroupAccessMetadataRequest.to_json()

# convert the object into a dict
upsert_portfolio_group_access_metadata_request_dict = upsert_portfolio_group_access_metadata_request_instance.to_dict()
# create an instance of UpsertPortfolioGroupAccessMetadataRequest from a dict
upsert_portfolio_group_access_metadata_request_form_dict = upsert_portfolio_group_access_metadata_request.from_dict(upsert_portfolio_group_access_metadata_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


