# ModelSelection

The combination of a library to use and a model in that library that defines which pricing code will evaluate instruments having a particular type/class. This allows us to control the model type and library for a given instrument.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**library** | **str** | The available values are: Lusid, RefinitivQps, RefinitivTracsWeb, VolMaster, IsdaCds, YieldBook, LusidCalc | 
**model** | **str** | The available values are: SimpleStatic, Discounting, VendorDefault, BlackScholes, ConstantTimeValueOfMoney, Bachelier, ForwardWithPoints, ForwardWithPointsUndiscounted, ForwardSpecifiedRate, ForwardSpecifiedRateUndiscounted, IndexNav, IndexPrice, InlinedIndex, ForwardFromCurve, ForwardFromCurveUndiscounted, BlackScholesDigital, BjerksundStensland1993, BondLookupPricer, FlexibleLoanPricer, CdsLookupPricer, LoanFacilityPricer | 
## Example

```python
from lusid.models.model_selection import ModelSelection
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, StrictStr, validator

library: StrictStr = "example_library"
model: StrictStr = "example_model"
model_selection_instance = ModelSelection(library=library, model=model)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

