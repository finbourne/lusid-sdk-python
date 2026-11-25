# CollateralSubstitutionConstituent

A single collateral instrument taking part in a FlexibleRepoCollateralSubstitutionEvent, either as outgoing  collateral being returned or as incoming collateral replacing it. Contains a reference to the instrument as a  NewInstrument object, an optional amount and the type of that amount (Units or Percentage of current units).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument** | [**NewInstrument**](NewInstrument.md) |  | 
**amount** | **float** | If AmountType is set to Units, this field represents the number of units of the instrument being transferred.  If AmountType is set to Percentage, this field represents the percentage of the repoed units of the instrument being transferred.  Required for outgoing collateral. For incoming collateral it is required when AdjustCollateralUnits is false;  the instrument is then held in the units given, so its AmountType must be Units. | [optional] 
**amount_type** | **str** | The type of amount represented by the Amount field.  I.e., does it represent a number of units or a percentage of the repoed units of the instrument?  Supported string (enumeration) values are: [Percentage, Units]. Defaults to Units. Must be Units for incoming  collateral. Available values: Percentage, Units. | [optional] 
## Example

```python
from lusid.models.collateral_substitution_constituent import CollateralSubstitutionConstituent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

instrument: NewInstrument
amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
amount_type: Optional[StrictStr] = "example_amount_type"
collateral_substitution_constituent_instance = CollateralSubstitutionConstituent(instrument=instrument, amount=amount, amount_type=amount_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

