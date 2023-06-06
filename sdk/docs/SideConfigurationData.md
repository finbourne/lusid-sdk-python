# SideConfigurationData

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
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.side_configuration_data import SideConfigurationData

# TODO update the JSON string below
json = "{}"
# create an instance of SideConfigurationData from a JSON string
side_configuration_data_instance = SideConfigurationData.from_json(json)
# print the JSON string representation of the object
print SideConfigurationData.to_json()

# convert the object into a dict
side_configuration_data_dict = side_configuration_data_instance.to_dict()
# create an instance of SideConfigurationData from a dict
side_configuration_data_form_dict = side_configuration_data.from_dict(side_configuration_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


