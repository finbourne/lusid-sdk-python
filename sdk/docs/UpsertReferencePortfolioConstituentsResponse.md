# UpsertReferencePortfolioConstituentsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.upsert_reference_portfolio_constituents_response import UpsertReferencePortfolioConstituentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertReferencePortfolioConstituentsResponse from a JSON string
upsert_reference_portfolio_constituents_response_instance = UpsertReferencePortfolioConstituentsResponse.from_json(json)
# print the JSON string representation of the object
print UpsertReferencePortfolioConstituentsResponse.to_json()

# convert the object into a dict
upsert_reference_portfolio_constituents_response_dict = upsert_reference_portfolio_constituents_response_instance.to_dict()
# create an instance of UpsertReferencePortfolioConstituentsResponse from a dict
upsert_reference_portfolio_constituents_response_form_dict = upsert_reference_portfolio_constituents_response.from_dict(upsert_reference_portfolio_constituents_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


