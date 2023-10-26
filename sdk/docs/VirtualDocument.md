# VirtualDocument

Virtual document consists of (potentially several) upserted documents.                The documents get parsed according to the provided data map on upsert, the collection of resulting values in  aggregated in a virtual document

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | [**StructuredResultDataId**](StructuredResultDataId.md) |  | [optional] 
**data** | [**List[VirtualDocumentRow]**](VirtualDocumentRow.md) | The data inside the document | [optional] 

## Example

```python
from lusid.models.virtual_document import VirtualDocument

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDocument from a JSON string
virtual_document_instance = VirtualDocument.from_json(json)
# print the JSON string representation of the object
print VirtualDocument.to_json()

# convert the object into a dict
virtual_document_dict = virtual_document_instance.to_dict()
# create an instance of VirtualDocument from a dict
virtual_document_form_dict = virtual_document.from_dict(virtual_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


