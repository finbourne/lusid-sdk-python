# CreateReferencePortfolioRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the reference portfolio. | 
**description** | **str** | A long form text description of the portfolio. | [optional] 
**code** | **str** | Unique identifier for the portfolio. | 
**created** | **datetime** | The original creation date, defaults to today if not specified when creating a portfolio. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | Portfolio properties to add to the portfolio. | [optional] 
**instrument_scopes** | **List[str]** | Instrument Scopes. | [optional] 
**base_currency** | **str** | The base currency of the transaction portfolio in ISO 4217 currency code format. | [optional] 

## Example

```python
from lusid.models.create_reference_portfolio_request import CreateReferencePortfolioRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateReferencePortfolioRequest from a JSON string
create_reference_portfolio_request_instance = CreateReferencePortfolioRequest.from_json(json)
# print the JSON string representation of the object
print CreateReferencePortfolioRequest.to_json()

# convert the object into a dict
create_reference_portfolio_request_dict = create_reference_portfolio_request_instance.to_dict()
# create an instance of CreateReferencePortfolioRequest from a dict
create_reference_portfolio_request_form_dict = create_reference_portfolio_request.from_dict(create_reference_portfolio_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


