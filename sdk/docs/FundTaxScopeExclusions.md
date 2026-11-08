# FundTaxScopeExclusions

What the UK chargeable-gains figures leave out of the pooled computation.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_types** | **List[str]** | Instrument types that stay on the portfolio&#39;s ordinary accounting method rather than being pooled, by name. | 
**leaf_outcomes** | **List[str]** | Disposal-leg outcomes the configured regime options disapply. Empty under the standard options. | 
**applied_in_figures** | **bool** | Whether the engine enforces these exclusions when building the pooled lots and gains. | 
## Example

```python
from lusid.models.fund_tax_scope_exclusions import FundTaxScopeExclusions
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

instrument_types: List[StrictStr] = # Replace with your value
leaf_outcomes: List[StrictStr] = # Replace with your value
applied_in_figures: StrictBool = # Replace with your value
applied_in_figures:StrictBool = True
fund_tax_scope_exclusions_instance = FundTaxScopeExclusions(instrument_types=instrument_types, leaf_outcomes=leaf_outcomes, applied_in_figures=applied_in_figures)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

