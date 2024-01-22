# AborRequest

The request used to create an Abor.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code given for the Abor. | 
**display_name** | **str** | The name of the Abor. | 
**description** | **str** | The description for the Abor. | [optional] 
**portfolio_ids** | [**List[PortfolioEntityId]**](PortfolioEntityId.md) | The list with the portfolio ids which are part of the Abor. Note: These must all have the same base currency. | 
**abor_configuration_id** | [**ResourceId**](ResourceId.md) |  | 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties for the Abor. | [optional] 

## Example

```python
from lusid.models.abor_request import AborRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AborRequest from a JSON string
abor_request_instance = AborRequest.from_json(json)
# print the JSON string representation of the object
print AborRequest.to_json()

# convert the object into a dict
abor_request_dict = abor_request_instance.to_dict()
# create an instance of AborRequest from a dict
abor_request_form_dict = abor_request.from_dict(abor_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


