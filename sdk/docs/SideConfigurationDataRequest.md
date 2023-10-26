# SideConfigurationDataRequest

Configuration needed to define a side. Sides are referenced by Label. Beyond that, other properties  can be used to reference either transaction fields, or transaction properties.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**side** | **str** | The side&#39;s label. | 
**security** | **str** | The security, or instrument. | 
**currency** | **str** | The currency. | 
**rate** | **str** | The rate. | 
**units** | **str** | The units. | 
**amount** | **str** | The amount. | 

## Example

```python
from lusid.models.side_configuration_data_request import SideConfigurationDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SideConfigurationDataRequest from a JSON string
side_configuration_data_request_instance = SideConfigurationDataRequest.from_json(json)
# print the JSON string representation of the object
print SideConfigurationDataRequest.to_json()

# convert the object into a dict
side_configuration_data_request_dict = side_configuration_data_request_instance.to_dict()
# create an instance of SideConfigurationDataRequest from a dict
side_configuration_data_request_form_dict = side_configuration_data_request.from_dict(side_configuration_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


