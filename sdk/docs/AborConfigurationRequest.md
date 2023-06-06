# AborConfigurationRequest

The request used to create an AborConfiguration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code given for the AborConfiguration. | 
**description** | **str** | The description for the AborConfiguration. | [optional] 
**name** | **str** | The given name for the AborConfiguration. | [optional] 
**recipe_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**chart_of_accounts_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | Properties to add to the AborConfiguration. | [optional] 

## Example

```python
from lusid.models.abor_configuration_request import AborConfigurationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AborConfigurationRequest from a JSON string
abor_configuration_request_instance = AborConfigurationRequest.from_json(json)
# print the JSON string representation of the object
print AborConfigurationRequest.to_json()

# convert the object into a dict
abor_configuration_request_dict = abor_configuration_request_instance.to_dict()
# create an instance of AborConfigurationRequest from a dict
abor_configuration_request_form_dict = abor_configuration_request.from_dict(abor_configuration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


