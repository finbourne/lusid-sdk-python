# QuoteId

The unique identifier of the quote.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote_series_id** | [**QuoteSeriesId**](QuoteSeriesId.md) |  | 
**effective_at** | **str** | The effective datetime or cut label at which the quote is valid from. | 
## Example

```python
from lusid.models.quote_id import QuoteId
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr

quote_series_id: QuoteSeriesId = # Replace with your value
effective_at: StrictStr = "example_effective_at"
quote_id_instance = QuoteId(quote_series_id=quote_series_id, effective_at=effective_at)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

