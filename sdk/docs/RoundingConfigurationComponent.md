# RoundingConfigurationComponent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rounding_type** | **str** | The type of rounding that should be used, eg: Up, Down, NearestRoundHalfAwayFromZero | 

## Example

```python
from lusid.models.rounding_configuration_component import RoundingConfigurationComponent

# TODO update the JSON string below
json = "{}"
# create an instance of RoundingConfigurationComponent from a JSON string
rounding_configuration_component_instance = RoundingConfigurationComponent.from_json(json)
# print the JSON string representation of the object
print RoundingConfigurationComponent.to_json()

# convert the object into a dict
rounding_configuration_component_dict = rounding_configuration_component_instance.to_dict()
# create an instance of RoundingConfigurationComponent from a dict
rounding_configuration_component_form_dict = rounding_configuration_component.from_dict(rounding_configuration_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


