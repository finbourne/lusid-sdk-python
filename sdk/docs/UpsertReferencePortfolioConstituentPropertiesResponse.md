# UpsertReferencePortfolioConstituentPropertiesResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | The updated collection of properties of the constituent. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.upsert_reference_portfolio_constituent_properties_response import UpsertReferencePortfolioConstituentPropertiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertReferencePortfolioConstituentPropertiesResponse from a JSON string
upsert_reference_portfolio_constituent_properties_response_instance = UpsertReferencePortfolioConstituentPropertiesResponse.from_json(json)
# print the JSON string representation of the object
print UpsertReferencePortfolioConstituentPropertiesResponse.to_json()

# convert the object into a dict
upsert_reference_portfolio_constituent_properties_response_dict = upsert_reference_portfolio_constituent_properties_response_instance.to_dict()
# create an instance of UpsertReferencePortfolioConstituentPropertiesResponse from a dict
upsert_reference_portfolio_constituent_properties_response_form_dict = upsert_reference_portfolio_constituent_properties_response.from_dict(upsert_reference_portfolio_constituent_properties_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


