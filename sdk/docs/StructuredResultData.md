# StructuredResultData

An item of structured result data that is to be inserted into Lusid. This will typically be a Json or Xml document that  contains a set of result data appropriate to a specific entity such as an instrument or potentially an index.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_format** | **str** | The format of the accompanying document. | 
**version** | **str** | The semantic version of the document format; MAJOR.MINOR.PATCH | [optional] 
**name** | **str** | The name or description for the document | [optional] 
**document** | **str** | The document that will be stored (or retrieved) and which describes a unit result data entity such as a set of prices or yields | 
**data_map_key** | [**DataMapKey**](DataMapKey.md) |  | [optional] 

## Example

```python
from lusid.models.structured_result_data import StructuredResultData

# TODO update the JSON string below
json = "{}"
# create an instance of StructuredResultData from a JSON string
structured_result_data_instance = StructuredResultData.from_json(json)
# print the JSON string representation of the object
print StructuredResultData.to_json()

# convert the object into a dict
structured_result_data_dict = structured_result_data_instance.to_dict()
# create an instance of StructuredResultData from a dict
structured_result_data_form_dict = structured_result_data.from_dict(structured_result_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


