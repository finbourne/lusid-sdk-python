# ReferenceData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_definitions** | [**List[FieldDefinition]**](FieldDefinition.md) |  | 
**values** | [**List[FieldValue]**](FieldValue.md) |  | 

## Example

```python
from lusid.models.reference_data import ReferenceData

# TODO update the JSON string below
json = "{}"
# create an instance of ReferenceData from a JSON string
reference_data_instance = ReferenceData.from_json(json)
# print the JSON string representation of the object
print ReferenceData.to_json()

# convert the object into a dict
reference_data_dict = reference_data_instance.to_dict()
# create an instance of ReferenceData from a dict
reference_data_form_dict = reference_data.from_dict(reference_data_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


