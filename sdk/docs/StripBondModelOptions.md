# StripBondModelOptions

Model options for StripBond pricing: how a strip's cash receipts are split between income and return of  capital. Set on the VendorModelRule for StripBond under the BondLookupPricer, SimpleStatic or  OverrideOnlyPricer model.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strip_accounting_choice** | **str** | How a StripBond&#39;s cash receipts are split between income and return of capital.  Null means CostRecovery: the effective yield is 0, every receipt returns capital until cost is recovered.  QuotedYield reads the strip&#39;s EffectiveYield quote at the parent flow&#39;s ex-date.  CashAsReceived applies no yield: each receipt is booked as the parent paid it, an interest-only strip&#39;s  cash as income and a principal-only strip&#39;s as return of capital.                Supported string (enumeration) values are: [CostRecovery, QuotedYield, CashAsReceived]. | [optional] 
**model_options_type** | **str** | Available values: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, CdsModelOptions, FlexibleLoanPricerOptions, HullWhiteModelOptions, BondLookupModelOptions, BondForwardModelOptions, SimpleModelOptions, StripBondModelOptions. | 
## Example

```python
from lusid.models.strip_bond_model_options import StripBondModelOptions
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

strip_accounting_choice: Optional[StrictStr] = "example_strip_accounting_choice"
model_options_type: StrictStr = "example_model_options_type"
strip_bond_model_options_instance = StripBondModelOptions(strip_accounting_choice=strip_accounting_choice, model_options_type=model_options_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

