# RecResultLinkKey

One item pairing that established a link between two rec results: the identifiers both results' items carried.  Exactly one of holdingId and transactionId is populated; taxLotId only ever accompanies a holdingId, and only  where the pairing was established at tax-lot precision.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**holding_id** | **str** | The holding both items carried, for a holding-keyed pairing. Null for a transaction-keyed one. | [optional] 
**tax_lot_id** | **str** | The tax lot both items carried within the holding, where the pairing was established at tax-lot precision. Null where it was established at holding precision, and always null for a transaction-keyed pairing. | [optional] 
**transaction_id** | **str** | The transaction both items carried, for a transaction-keyed pairing. Null for a holding-keyed one. | [optional] 
## Example

```python
from lusid.models.rec_result_link_key import RecResultLinkKey
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

holding_id: Optional[StrictStr] = "example_holding_id"
tax_lot_id: Optional[StrictStr] = "example_tax_lot_id"
transaction_id: Optional[StrictStr] = "example_transaction_id"
rec_result_link_key_instance = RecResultLinkKey(holding_id=holding_id, tax_lot_id=tax_lot_id, transaction_id=transaction_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

