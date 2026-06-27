# AccountedQuote

The Valuation Point quote response for a Fund, including the origin of the quote relative to the Valuation Point period.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote** | [**Quote**](Quote.md) |  | [optional] 
**valuation_point_origin** | **str** | Designates if the quote was originally part of the Valuation Point or if it was added as part of a Complex Close action. Available values: None, Original, Added, OriginalAndAdded. | [optional] 
**added_origin_valuation_point_code** | **str** | The Valuation Point code, only for quotes added as part of a Complex Close action. | [optional] 
**added_origin_valuation_point_variant_code** | **str** | The Valuation Point variant code, only for quotes added as part of a Complex Close action. | [optional] 
## Example

```python
from lusid.models.accounted_quote import AccountedQuote
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

quote: Optional[Quote] = None
valuation_point_origin: Optional[StrictStr] = "example_valuation_point_origin"
added_origin_valuation_point_code: Optional[StrictStr] = "example_added_origin_valuation_point_code"
added_origin_valuation_point_variant_code: Optional[StrictStr] = "example_added_origin_valuation_point_variant_code"
accounted_quote_instance = AccountedQuote(quote=quote, valuation_point_origin=valuation_point_origin, added_origin_valuation_point_code=added_origin_valuation_point_code, added_origin_valuation_point_variant_code=added_origin_valuation_point_variant_code)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

