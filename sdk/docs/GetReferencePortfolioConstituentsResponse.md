# GetReferencePortfolioConstituentsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_from** | **datetime** |  | 
**weight_type** | **str** | The available values are: Static, Floating, Periodical | 
**period_type** | **str** | The available values are: Daily, Weekly, Monthly, Quarterly, Annually | [optional] 
**period_count** | **int** |  | [optional] 
**constituents** | [**List[ReferencePortfolioConstituent]**](ReferencePortfolioConstituent.md) | Set of constituents (instrument/weight pairings) | 
**href** | **str** | The Uri that returns the same result as the original request,  but may include resolved as at time(s). | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.get_reference_portfolio_constituents_response import GetReferencePortfolioConstituentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetReferencePortfolioConstituentsResponse from a JSON string
get_reference_portfolio_constituents_response_instance = GetReferencePortfolioConstituentsResponse.from_json(json)
# print the JSON string representation of the object
print GetReferencePortfolioConstituentsResponse.to_json()

# convert the object into a dict
get_reference_portfolio_constituents_response_dict = get_reference_portfolio_constituents_response_instance.to_dict()
# create an instance of GetReferencePortfolioConstituentsResponse from a dict
get_reference_portfolio_constituents_response_form_dict = get_reference_portfolio_constituents_response.from_dict(get_reference_portfolio_constituents_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


