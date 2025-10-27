# UpsertCreditSupportAnnexRequest

Credit Support Annex information. The interaction in terms of margining requirements between a set of trades for a given counterparty.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credit_support_annex** | [**CreditSupportAnnex**](CreditSupportAnnex.md) |  | [optional] 
## Example

```python
from lusid.models.upsert_credit_support_annex_request import UpsertCreditSupportAnnexRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

credit_support_annex: Optional[CreditSupportAnnex] = # Replace with your value
upsert_credit_support_annex_request_instance = UpsertCreditSupportAnnexRequest(credit_support_annex=credit_support_annex)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

