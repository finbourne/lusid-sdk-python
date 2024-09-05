# BatchUpsertPortfolioAccessMetadataResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portfolios_with_metadata** | [**Dict[str, MetadataKeyValueResponse]**](MetadataKeyValueResponse.md) | The set of portfolios with the access control metadata | 

## Example

```python
from lusid.models.batch_upsert_portfolio_access_metadata_response import BatchUpsertPortfolioAccessMetadataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BatchUpsertPortfolioAccessMetadataResponse from a JSON string
batch_upsert_portfolio_access_metadata_response_instance = BatchUpsertPortfolioAccessMetadataResponse.from_json(json)
# print the JSON string representation of the object
print BatchUpsertPortfolioAccessMetadataResponse.to_json()

# convert the object into a dict
batch_upsert_portfolio_access_metadata_response_dict = batch_upsert_portfolio_access_metadata_response_instance.to_dict()
# create an instance of BatchUpsertPortfolioAccessMetadataResponse from a dict
batch_upsert_portfolio_access_metadata_response_form_dict = batch_upsert_portfolio_access_metadata_response.from_dict(batch_upsert_portfolio_access_metadata_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


