# VirtualRow

Rows identified by the composite id, based on the data maps

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**row_id** | **Dict[str, str]** | The identifier for the row. This is keyed by address keys, and values obtained through applying the data map to the documents. | [optional] 
**row_data** | [**Dict[str, ResultValue]**](ResultValue.md) | The data for the particular row | [optional] 

## Example

```python
from lusid.models.virtual_row import VirtualRow

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualRow from a JSON string
virtual_row_instance = VirtualRow.from_json(json)
# print the JSON string representation of the object
print VirtualRow.to_json()

# convert the object into a dict
virtual_row_dict = virtual_row_instance.to_dict()
# create an instance of VirtualRow from a dict
virtual_row_form_dict = virtual_row.from_dict(virtual_row_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


