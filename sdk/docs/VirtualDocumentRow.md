# VirtualDocumentRow

Rows identified by the composite id, based on the data maps

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**row_id** | **Dict[str, str]** | The identifier for the row. This is keyed by address keys, and values obtained through applying the data map to the documents. | [optional] 
**row_data** | [**GroupedResultOfAddressKey**](GroupedResultOfAddressKey.md) |  | [optional] 

## Example

```python
from lusid.models.virtual_document_row import VirtualDocumentRow

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDocumentRow from a JSON string
virtual_document_row_instance = VirtualDocumentRow.from_json(json)
# print the JSON string representation of the object
print VirtualDocumentRow.to_json()

# convert the object into a dict
virtual_document_row_dict = virtual_document_row_instance.to_dict()
# create an instance of VirtualDocumentRow from a dict
virtual_document_row_form_dict = virtual_document_row.from_dict(virtual_document_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


