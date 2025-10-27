# Quote

The quote id, value and lineage of the quotes all keyed by a unique correlation id.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote_id** | [**QuoteId**](QuoteId.md) |  | 
**metric_value** | [**MetricValue**](MetricValue.md) |  | [optional] 
**lineage** | **str** | Description of the quote&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;. | [optional] 
**cut_label** | **str** | The cut label that this quote was updated or inserted with. | [optional] 
**uploaded_by** | **str** | The unique id of the user that updated or inserted the quote. | 
**as_at** | **datetime** | The asAt datetime at which the quote was committed to LUSID. | 
**scale_factor** | **float** | An optional scale factor for non-standard scaling of quotes against the instrument. For example, if you wish the quote&#39;s Value to be scaled down by a factor of 100, enter 100. If not supplied, the default ScaleFactor is 1. | [optional] 
## Example

```python
from lusid.models.quote import Quote
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

quote_id: QuoteId = # Replace with your value
metric_value: Optional[MetricValue] = # Replace with your value
lineage: Optional[StrictStr] = "example_lineage"
cut_label: Optional[StrictStr] = "example_cut_label"
uploaded_by: StrictStr = "example_uploaded_by"
as_at: datetime = # Replace with your value
scale_factor: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
quote_instance = Quote(quote_id=quote_id, metric_value=metric_value, lineage=lineage, cut_label=cut_label, uploaded_by=uploaded_by, as_at=as_at, scale_factor=scale_factor)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

