# AnnulSingleStructuredDataResponse

The response to a request to annul (delete) a set of structured data from Lusid. This might have been for market data or some other structured entity.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**value** | **datetime** | The time at which the identifier was annulled | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.annul_single_structured_data_response import AnnulSingleStructuredDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AnnulSingleStructuredDataResponse from a JSON string
annul_single_structured_data_response_instance = AnnulSingleStructuredDataResponse.from_json(json)
# print the JSON string representation of the object
print AnnulSingleStructuredDataResponse.to_json()

# convert the object into a dict
annul_single_structured_data_response_dict = annul_single_structured_data_response_instance.to_dict()
# create an instance of AnnulSingleStructuredDataResponse from a dict
annul_single_structured_data_response_form_dict = annul_single_structured_data_response.from_dict(annul_single_structured_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


