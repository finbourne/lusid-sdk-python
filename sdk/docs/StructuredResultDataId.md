# StructuredResultDataId

An identifier that uniquely describes an item of structured result data such as the risk to an interest curve or a set of yields or analytics on an index.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | The platform or vendor that provided the structured result data, e.g. &#39;client&#39;. This is primarily of interest when data could have been sourced from multiple sources | 
**code** | **str** | The identifier for the entity that this id describes. It could be an index, instrument or other form of structured data | [optional] 
**effective_at** | **str** | The effectiveAt or cut label that this item of structured result data is/was updated/inserted with. | [optional] 
**result_type** | **str** | An identifier that denotes the class of data that the id points to. This is not the same as the format, but a more generic identifier such as &#39;risk result&#39;, &#39;cashflow&#39;, &#39;index&#39; or similar. | [optional] 

## Example

```python
from lusid.models.structured_result_data_id import StructuredResultDataId

# TODO update the JSON string below
json = "{}"
# create an instance of StructuredResultDataId from a JSON string
structured_result_data_id_instance = StructuredResultDataId.from_json(json)
# print the JSON string representation of the object
print StructuredResultDataId.to_json()

# convert the object into a dict
structured_result_data_id_dict = structured_result_data_id_instance.to_dict()
# create an instance of StructuredResultDataId from a dict
structured_result_data_id_form_dict = structured_result_data_id.from_dict(structured_result_data_id_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


