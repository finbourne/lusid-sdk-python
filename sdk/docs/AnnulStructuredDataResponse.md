# AnnulStructuredDataResponse

The response to a request to annul (delete) a set of structured data from Lusid. This might have been for market data or some other structured entity.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**values** | **Dict[str, datetime]** | The set of values that were removed. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The set of values where removal failed, with a description as to why that is the case, e.g. badly formed request | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.annul_structured_data_response import AnnulStructuredDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AnnulStructuredDataResponse from a JSON string
annul_structured_data_response_instance = AnnulStructuredDataResponse.from_json(json)
# print the JSON string representation of the object
print AnnulStructuredDataResponse.to_json()

# convert the object into a dict
annul_structured_data_response_dict = annul_structured_data_response_instance.to_dict()
# create an instance of AnnulStructuredDataResponse from a dict
annul_structured_data_response_form_dict = annul_structured_data_response.from_dict(annul_structured_data_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


