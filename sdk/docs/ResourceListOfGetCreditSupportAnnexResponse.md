# ResourceListOfGetCreditSupportAnnexResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[GetCreditSupportAnnexResponse]**](GetCreditSupportAnnexResponse.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_get_credit_support_annex_response import ResourceListOfGetCreditSupportAnnexResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfGetCreditSupportAnnexResponse from a JSON string
resource_list_of_get_credit_support_annex_response_instance = ResourceListOfGetCreditSupportAnnexResponse.from_json(json)
# print the JSON string representation of the object
print ResourceListOfGetCreditSupportAnnexResponse.to_json()

# convert the object into a dict
resource_list_of_get_credit_support_annex_response_dict = resource_list_of_get_credit_support_annex_response_instance.to_dict()
# create an instance of ResourceListOfGetCreditSupportAnnexResponse from a dict
resource_list_of_get_credit_support_annex_response_form_dict = resource_list_of_get_credit_support_annex_response.from_dict(resource_list_of_get_credit_support_annex_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


