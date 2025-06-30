# UpsertCounterpartyAgreementRequest

Counterparty Agreement that is to be stored in the convention data store.  There must be only one of these present.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counterparty_agreement** | [**CounterpartyAgreement**](CounterpartyAgreement.md) |  | 
## Example

```python
from lusid.models.upsert_counterparty_agreement_request import UpsertCounterpartyAgreementRequest
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field

counterparty_agreement: CounterpartyAgreement = # Replace with your value
upsert_counterparty_agreement_request_instance = UpsertCounterpartyAgreementRequest(counterparty_agreement=counterparty_agreement)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

