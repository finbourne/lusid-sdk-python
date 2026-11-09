# UpsertTaxTreatmentOverrideRequest

Pins an instrument to a treatment leaf in place of the system-derived one.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**treatment** | **str** | The treatment leaf to pin the instrument to, replacing the system-derived one. Available values: OutsideBlagab, LoanRelationship, IndexLinkedGilt, PrivateEquity, RealEstate, FinancialFuture, PooledDerivative, DerivativeProfitAndLoss, NonTransparentScheme, BondFund, TransparentScheme, StandardEquity, Exempt. | 
**effective_at** | **datetime** | The effective date the override applies from. Defaults to the start of time if not specified. | [optional] 
## Example

```python
from lusid.models.upsert_tax_treatment_override_request import UpsertTaxTreatmentOverrideRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

treatment: StrictStr = "example_treatment"
effective_at: Optional[datetime] = # Replace with your value
upsert_tax_treatment_override_request_instance = UpsertTaxTreatmentOverrideRequest(treatment=treatment, effective_at=effective_at)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

