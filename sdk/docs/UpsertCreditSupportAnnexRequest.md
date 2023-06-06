# UpsertCreditSupportAnnexRequest

Credit Support Annex information. The interaction in terms of margining requirements between a set of trades for a given counterparty.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credit_support_annex** | [**CreditSupportAnnex**](CreditSupportAnnex.md) |  | [optional] 

## Example

```python
from lusid.models.upsert_credit_support_annex_request import UpsertCreditSupportAnnexRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertCreditSupportAnnexRequest from a JSON string
upsert_credit_support_annex_request_instance = UpsertCreditSupportAnnexRequest.from_json(json)
# print the JSON string representation of the object
print UpsertCreditSupportAnnexRequest.to_json()

# convert the object into a dict
upsert_credit_support_annex_request_dict = upsert_credit_support_annex_request_instance.to_dict()
# create an instance of UpsertCreditSupportAnnexRequest from a dict
upsert_credit_support_annex_request_form_dict = upsert_credit_support_annex_request.from_dict(upsert_credit_support_annex_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


