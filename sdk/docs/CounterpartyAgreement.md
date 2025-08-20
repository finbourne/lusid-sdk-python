# CounterpartyAgreement

Represents the legal agreement between two parties engaged in an OTC transaction. A typical example would be a 2002 ISDA Master Agreement, signed by two legal entities on a given date.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | A user-defined display label for the Counterparty Agreement. | 
**agreement_type** | **str** | A user-defined field to capture the type of agreement this represents. Examples might be \&quot;ISDA 2002 Master Agreement\&quot; or \&quot;ISDA 1992 Master Agreement\&quot;. | 
**counterparty_signatory** | [**CounterpartySignatory**](CounterpartySignatory.md) |  | 
**dated_as_of** | **datetime** | The date on which the CounterpartyAgreement was signed by both parties. | 
**credit_support_annex_id** | [**ResourceId**](ResourceId.md) |  | 
**id** | [**ResourceId**](ResourceId.md) |  | 
## Example

```python
from lusid.models.counterparty_agreement import CounterpartyAgreement
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr
from datetime import datetime
display_name: StrictStr = "example_display_name"
agreement_type: StrictStr = "example_agreement_type"
counterparty_signatory: CounterpartySignatory = # Replace with your value
dated_as_of: datetime = # Replace with your value
credit_support_annex_id: ResourceId = # Replace with your value
id: ResourceId = # Replace with your value
counterparty_agreement_instance = CounterpartyAgreement(display_name=display_name, agreement_type=agreement_type, counterparty_signatory=counterparty_signatory, dated_as_of=dated_as_of, credit_support_annex_id=credit_support_annex_id, id=id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

