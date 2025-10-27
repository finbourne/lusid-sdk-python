# AggregationOptions

Options for controlling the default aspects and behaviour of the aggregation.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_ansi_like_syntax** | **bool** | Should the aggregation behave like ANSI Sql or MySql with respect to a conceptual request which is equivalent to \&quot;select a,sum(a) from results\&quot;;  ANSI Sql would report an error if a was not unique where MySql would simply view a,suma(a) as equivalent to firstof(a),sum(a). | [optional] 
**allow_partial_entitlement_success** | **bool** | In the case of valuing a portfolio group where some, but not all entitlements fail, should the aggregation return the valuations  applied only to those portfolios where entitlements checks succeeded. | [optional] 
**apply_iso4217_rounding** | **bool** | Various results that are units of currency might need to be rounded.  This will round according to the ISO4217 standard number of decimal places for a currency. | [optional] 
## Example

```python
from lusid.models.aggregation_options import AggregationOptions
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

use_ansi_like_syntax: Optional[StrictBool] = # Replace with your value
use_ansi_like_syntax:Optional[StrictBool] = None
allow_partial_entitlement_success: Optional[StrictBool] = # Replace with your value
allow_partial_entitlement_success:Optional[StrictBool] = None
apply_iso4217_rounding: Optional[StrictBool] = # Replace with your value
apply_iso4217_rounding:Optional[StrictBool] = None
aggregation_options_instance = AggregationOptions(use_ansi_like_syntax=use_ansi_like_syntax, allow_partial_entitlement_success=allow_partial_entitlement_success, apply_iso4217_rounding=apply_iso4217_rounding)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

