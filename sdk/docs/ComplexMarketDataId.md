# ComplexMarketDataId

An identifier that uniquely describes an item of complex market data such as an interest rate curve or volatility surface.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | The platform or vendor that provided the complex market data, e.g. &#39;DataScope&#39;, &#39;LUSID&#39;, etc. | 
**price_source** | **str** | The source or originator of the complex market data, e.g. a bank or financial institution. | [optional] 
**lineage** | **str** | This is obsolete. It is not used, it will not be stored, and has no effects.  If you wish to attach a Lineage to your ComplexMarketData,  you should provide it in the optional Lineage field in the ComplexMarketData class. | [optional] 
**effective_at** | **str** | The effectiveAt or cut label that this item of complex market data is/was updated/inserted with. | [optional] 
**market_asset** | **str** | The name of the market entity that the document represents | 
## Example

```python
from lusid.models.complex_market_data_id import ComplexMarketDataId
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

provider: StrictStr = "example_provider"
price_source: Optional[StrictStr] = "example_price_source"
lineage: Optional[StrictStr] = "example_lineage"
effective_at: Optional[StrictStr] = "example_effective_at"
market_asset: StrictStr = "example_market_asset"
complex_market_data_id_instance = ComplexMarketDataId(provider=provider, price_source=price_source, lineage=lineage, effective_at=effective_at, market_asset=market_asset)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

