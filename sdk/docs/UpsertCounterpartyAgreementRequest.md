# UpsertCounterpartyAgreementRequest

Counterparty Agreement that is to be stored in the convention data store.  There must be only one of these present.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counterparty_agreement** | [**CounterpartyAgreement**](CounterpartyAgreement.md) |  | 

## Example

```python
from lusid.models.upsert_counterparty_agreement_request import UpsertCounterpartyAgreementRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertCounterpartyAgreementRequest from a JSON string
upsert_counterparty_agreement_request_instance = UpsertCounterpartyAgreementRequest.from_json(json)
# print the JSON string representation of the object
print UpsertCounterpartyAgreementRequest.to_json()

# convert the object into a dict
upsert_counterparty_agreement_request_dict = upsert_counterparty_agreement_request_instance.to_dict()
# create an instance of UpsertCounterpartyAgreementRequest from a dict
upsert_counterparty_agreement_request_form_dict = upsert_counterparty_agreement_request.from_dict(upsert_counterparty_agreement_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


