# UpsertReferencePortfolioConstituentPropertiesRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifiers** | **Dict[str, str]** | A set of instrument identifiers that can resolve the constituent to a unique instrument. | 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | The updated collection of properties of the constituent. | 

## Example

```python
from lusid.models.upsert_reference_portfolio_constituent_properties_request import UpsertReferencePortfolioConstituentPropertiesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertReferencePortfolioConstituentPropertiesRequest from a JSON string
upsert_reference_portfolio_constituent_properties_request_instance = UpsertReferencePortfolioConstituentPropertiesRequest.from_json(json)
# print the JSON string representation of the object
print UpsertReferencePortfolioConstituentPropertiesRequest.to_json()

# convert the object into a dict
upsert_reference_portfolio_constituent_properties_request_dict = upsert_reference_portfolio_constituent_properties_request_instance.to_dict()
# create an instance of UpsertReferencePortfolioConstituentPropertiesRequest from a dict
upsert_reference_portfolio_constituent_properties_request_form_dict = upsert_reference_portfolio_constituent_properties_request.from_dict(upsert_reference_portfolio_constituent_properties_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


