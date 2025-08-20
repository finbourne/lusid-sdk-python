# FxConventions

The conventions for the calculation of FX fixings, where the fixing rate is expected to be the amount of DomCcy per unit of FgnCcy. As an example, assume the required fixing is the WM/R 4pm mid closing rate for the USD amount per 1 EUR. This is published with RIC EURUSDFIXM=WM, which would be the FixingReference, with FgnCcy EUR and DomCcy USD.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fgn_ccy** | **str** | The foreign currency | 
**dom_ccy** | **str** | The domestic currency | 
**fixing_reference** | **str** | The reference name used to find the desired quote | 
## Example

```python
from lusid.models.fx_conventions import FxConventions
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, StrictStr, constr

fgn_ccy: StrictStr = "example_fgn_ccy"
dom_ccy: StrictStr = "example_dom_ccy"
fixing_reference: StrictStr = "example_fixing_reference"
fx_conventions_instance = FxConventions(fgn_ccy=fgn_ccy, dom_ccy=dom_ccy, fixing_reference=fixing_reference)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

