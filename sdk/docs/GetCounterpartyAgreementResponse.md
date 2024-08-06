# GetCounterpartyAgreementResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**value** | [**CounterpartyAgreement**](CounterpartyAgreement.md) |  | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The counterparty agreement that could not be retrieved along with a reason for failure. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.get_counterparty_agreement_response import GetCounterpartyAgreementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCounterpartyAgreementResponse from a JSON string
get_counterparty_agreement_response_instance = GetCounterpartyAgreementResponse.from_json(json)
# print the JSON string representation of the object
print GetCounterpartyAgreementResponse.to_json()

# convert the object into a dict
get_counterparty_agreement_response_dict = get_counterparty_agreement_response_instance.to_dict()
# create an instance of GetCounterpartyAgreementResponse from a dict
get_counterparty_agreement_response_form_dict = get_counterparty_agreement_response.from_dict(get_counterparty_agreement_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


