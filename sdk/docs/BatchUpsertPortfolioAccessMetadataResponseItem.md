# BatchUpsertPortfolioAccessMetadataResponseItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**metadata** | **Dict[str, List[AccessMetadataValue]]** |  | 

## Example

```python
from lusid.models.batch_upsert_portfolio_access_metadata_response_item import BatchUpsertPortfolioAccessMetadataResponseItem

# TODO update the JSON string below
json = "{}"
# create an instance of BatchUpsertPortfolioAccessMetadataResponseItem from a JSON string
batch_upsert_portfolio_access_metadata_response_item_instance = BatchUpsertPortfolioAccessMetadataResponseItem.from_json(json)
# print the JSON string representation of the object
print BatchUpsertPortfolioAccessMetadataResponseItem.to_json()

# convert the object into a dict
batch_upsert_portfolio_access_metadata_response_item_dict = batch_upsert_portfolio_access_metadata_response_item_instance.to_dict()
# create an instance of BatchUpsertPortfolioAccessMetadataResponseItem from a dict
batch_upsert_portfolio_access_metadata_response_item_form_dict = batch_upsert_portfolio_access_metadata_response_item.from_dict(batch_upsert_portfolio_access_metadata_response_item_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


