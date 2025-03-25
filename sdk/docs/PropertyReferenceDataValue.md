# PropertyReferenceDataValue

The ReferenceData relevant to the property. The ReferenceData is taken from the DataType on the PropertyDefinition that defines the Property.  Only ReferenceData where the ReferenceData value matches the Property value is included.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**string_value** | **str** |  | [optional] 
**numeric_value** | **float** |  | [optional] 

## Example

```python
from lusid.models.property_reference_data_value import PropertyReferenceDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyReferenceDataValue from a JSON string
property_reference_data_value_instance = PropertyReferenceDataValue.from_json(json)
# print the JSON string representation of the object
print PropertyReferenceDataValue.to_json()

# convert the object into a dict
property_reference_data_value_dict = property_reference_data_value_instance.to_dict()
# create an instance of PropertyReferenceDataValue from a dict
property_reference_data_value_form_dict = property_reference_data_value.from_dict(property_reference_data_value_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


