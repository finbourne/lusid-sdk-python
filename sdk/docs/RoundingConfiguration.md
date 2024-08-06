# RoundingConfiguration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_units** | [**RoundingConfigurationComponent**](RoundingConfigurationComponent.md) |  | [optional] 

## Example

```python
from lusid.models.rounding_configuration import RoundingConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of RoundingConfiguration from a JSON string
rounding_configuration_instance = RoundingConfiguration.from_json(json)
# print the JSON string representation of the object
print RoundingConfiguration.to_json()

# convert the object into a dict
rounding_configuration_dict = rounding_configuration_instance.to_dict()
# create an instance of RoundingConfiguration from a dict
rounding_configuration_form_dict = rounding_configuration.from_dict(rounding_configuration_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


