# ExternalFeeComponentFilter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_id** | **str** |  | 
**filter** | **str** |  | 
**applies_to** | **str** |  | 

## Example

```python
from lusid.models.external_fee_component_filter import ExternalFeeComponentFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalFeeComponentFilter from a JSON string
external_fee_component_filter_instance = ExternalFeeComponentFilter.from_json(json)
# print the JSON string representation of the object
print ExternalFeeComponentFilter.to_json()

# convert the object into a dict
external_fee_component_filter_dict = external_fee_component_filter_instance.to_dict()
# create an instance of ExternalFeeComponentFilter from a dict
external_fee_component_filter_form_dict = external_fee_component_filter.from_dict(external_fee_component_filter_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


