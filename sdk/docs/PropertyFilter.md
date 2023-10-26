# PropertyFilter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | **str** | The key that uniquely identifies a queryable address in Lusid. | [optional] 
**operator** | **str** | The available values are: Equals, NotEquals, GreaterThan, GreaterThanOrEqualTo, LessThan, LessThanOrEqualTo, In | [optional] 
**right** | **object** |  | [optional] 
**right_operand_type** | **str** | The available values are: Absolute, Property | [optional] 

## Example

```python
from lusid.models.property_filter import PropertyFilter

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyFilter from a JSON string
property_filter_instance = PropertyFilter.from_json(json)
# print the JSON string representation of the object
print PropertyFilter.to_json()

# convert the object into a dict
property_filter_dict = property_filter_instance.to_dict()
# create an instance of PropertyFilter from a dict
property_filter_form_dict = property_filter.from_dict(property_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


