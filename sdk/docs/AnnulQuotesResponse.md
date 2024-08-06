# AnnulQuotesResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**values** | **Dict[str, datetime]** | The quotes which have been successfully deleted along with the asAt datetime at which the deletion was committed to LUSID. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The quotes that could not be deleted along with a reason for their failure. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.annul_quotes_response import AnnulQuotesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AnnulQuotesResponse from a JSON string
annul_quotes_response_instance = AnnulQuotesResponse.from_json(json)
# print the JSON string representation of the object
print AnnulQuotesResponse.to_json()

# convert the object into a dict
annul_quotes_response_dict = annul_quotes_response_instance.to_dict()
# create an instance of AnnulQuotesResponse from a dict
annul_quotes_response_form_dict = annul_quotes_response.from_dict(annul_quotes_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


