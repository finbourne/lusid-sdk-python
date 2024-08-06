# UpsertReferencePortfolioConstituentsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_from** | **str** | The first date from which the weights will apply | 
**weight_type** | **str** | The available values are: Static, Floating, Periodical | 
**period_type** | **str** | The available values are: Daily, Weekly, Monthly, Quarterly, Annually | [optional] 
**period_count** | **int** |  | [optional] 
**constituents** | [**List[ReferencePortfolioConstituentRequest]**](ReferencePortfolioConstituentRequest.md) | Set of constituents (instrument/weight pairings) | 

## Example

```python
from lusid.models.upsert_reference_portfolio_constituents_request import UpsertReferencePortfolioConstituentsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertReferencePortfolioConstituentsRequest from a JSON string
upsert_reference_portfolio_constituents_request_instance = UpsertReferencePortfolioConstituentsRequest.from_json(json)
# print the JSON string representation of the object
print UpsertReferencePortfolioConstituentsRequest.to_json()

# convert the object into a dict
upsert_reference_portfolio_constituents_request_dict = upsert_reference_portfolio_constituents_request_instance.to_dict()
# create an instance of UpsertReferencePortfolioConstituentsRequest from a dict
upsert_reference_portfolio_constituents_request_form_dict = upsert_reference_portfolio_constituents_request.from_dict(upsert_reference_portfolio_constituents_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


