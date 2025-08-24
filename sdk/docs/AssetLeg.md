# AssetLeg

The underlying instrument representing one side of the TRS and its pay-receive direction.                Note that TRS currently only supports an asset of Bond or ComplexBond, no other instruments are allowed.  Support for additional instrument types will be added in the future.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | [**LusidInstrument**](LusidInstrument.md) |  | 
**pay_receive** | **str** | Either Pay or Receive stating direction of the asset in the swap.    Supported string (enumeration) values are: [Pay, Receive]. | 
## Example

```python
from lusid.models.asset_leg import AssetLeg
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr

asset: LusidInstrument = # Replace with your value
pay_receive: StrictStr = "example_pay_receive"
asset_leg_instance = AssetLeg(asset=asset, pay_receive=pay_receive)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

