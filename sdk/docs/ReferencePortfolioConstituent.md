# ReferencePortfolioConstituent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_identifiers** | **Dict[str, str]** | Unique instrument identifiers | [optional] 
**instrument_uid** | **str** | LUSID&#39;s internal unique instrument identifier, resolved from the instrument identifiers | 
**currency** | **str** |  | 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Properties associated with the constituent | [optional] 
**weight** | **float** |  | 
**floating_weight** | **float** |  | [optional] 
**instrument_scope** | **str** |  | [optional] 

## Example

```python
from lusid.models.reference_portfolio_constituent import ReferencePortfolioConstituent

# TODO update the JSON string below
json = "{}"
# create an instance of ReferencePortfolioConstituent from a JSON string
reference_portfolio_constituent_instance = ReferencePortfolioConstituent.from_json(json)
# print the JSON string representation of the object
print ReferencePortfolioConstituent.to_json()

# convert the object into a dict
reference_portfolio_constituent_dict = reference_portfolio_constituent_instance.to_dict()
# create an instance of ReferencePortfolioConstituent from a dict
reference_portfolio_constituent_form_dict = reference_portfolio_constituent.from_dict(reference_portfolio_constituent_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


