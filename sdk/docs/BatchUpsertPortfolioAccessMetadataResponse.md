# BatchUpsertPortfolioAccessMetadataResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**Dict[str, BatchUpsertPortfolioAccessMetadataResponseItem]**](BatchUpsertPortfolioAccessMetadataResponseItem.md) | The items have been successfully updated or created. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The items that could not be updated or created along with a reason for their failure. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

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


