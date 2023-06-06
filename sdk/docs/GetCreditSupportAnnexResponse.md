# GetCreditSupportAnnexResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**value** | [**CreditSupportAnnex**](CreditSupportAnnex.md) |  | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The credit support annex that could not be updated or inserted along with a reason for failure. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.get_credit_support_annex_response import GetCreditSupportAnnexResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCreditSupportAnnexResponse from a JSON string
get_credit_support_annex_response_instance = GetCreditSupportAnnexResponse.from_json(json)
# print the JSON string representation of the object
print GetCreditSupportAnnexResponse.to_json()

# convert the object into a dict
get_credit_support_annex_response_dict = get_credit_support_annex_response_instance.to_dict()
# create an instance of GetCreditSupportAnnexResponse from a dict
get_credit_support_annex_response_form_dict = get_credit_support_annex_response.from_dict(get_credit_support_annex_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


