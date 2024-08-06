# ReferencePortfolioConstituentRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_identifiers** | **Dict[str, str]** | Unique instrument identifiers | 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) |  | [optional] 
**weight** | **float** |  | 
**currency** | **str** |  | [optional] 

## Example

```python
from lusid.models.reference_portfolio_constituent_request import ReferencePortfolioConstituentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReferencePortfolioConstituentRequest from a JSON string
reference_portfolio_constituent_request_instance = ReferencePortfolioConstituentRequest.from_json(json)
# print the JSON string representation of the object
print ReferencePortfolioConstituentRequest.to_json()

# convert the object into a dict
reference_portfolio_constituent_request_dict = reference_portfolio_constituent_request_instance.to_dict()
# create an instance of ReferencePortfolioConstituentRequest from a dict
reference_portfolio_constituent_request_form_dict = reference_portfolio_constituent_request.from_dict(reference_portfolio_constituent_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


