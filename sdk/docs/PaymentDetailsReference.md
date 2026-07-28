# PaymentDetailsReference

A pointer to a Payment Details relational dataset series for a payor or payee entity.  No PII is stored here — bank account details are resolved at read time from the referenced series.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**series_scope** | **str** | The scope of the relational datapoint. May differ from the scope of the dataset definition. | 
**applicable_entity** | [**PaymentDetailsApplicableEntity**](PaymentDetailsApplicableEntity.md) |  | 
**series_identifiers** | [**PaymentDetailsSeriesIdentifiers**](PaymentDetailsSeriesIdentifiers.md) |  | 
**effective_date** | **datetime** | The effective date of the relational datapoint observation to retrieve. ISO 8601 datetime. | 
**as_at_date** | **datetime** | The as-at date of the relational datapoint observation to retrieve. ISO 8601 datetime. | 
## Example

```python
from lusid.models.payment_details_reference import PaymentDetailsReference
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

series_scope: StrictStr = "example_series_scope"
applicable_entity: PaymentDetailsApplicableEntity = # Replace with your value
series_identifiers: PaymentDetailsSeriesIdentifiers = # Replace with your value
effective_date: datetime = # Replace with your value
as_at_date: datetime = # Replace with your value
payment_details_reference_instance = PaymentDetailsReference(series_scope=series_scope, applicable_entity=applicable_entity, series_identifiers=series_identifiers, effective_date=effective_date, as_at_date=as_at_date)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

