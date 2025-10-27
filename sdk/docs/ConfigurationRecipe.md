# ConfigurationRecipe

The Configuration or Calculation Recipe controls how LUSID processes a given request.  This can be used to change where market data used in pricing is loaded from and in what order, or which model is used to  price a given instrument as well as how aggregation will process the produced results.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The scope used when updating or inserting the Configuration Recipe. | 
**code** | **str** | User given string name (code) to identify the recipe. | 
**market** | [**MarketContext**](MarketContext.md) |  | [optional] 
**pricing** | [**PricingContext**](PricingContext.md) |  | [optional] 
**aggregation** | [**AggregationContext**](AggregationContext.md) |  | [optional] 
**description** | **str** | User can assign a description to understand more humanly the recipe. | [optional] 
**holding** | [**HoldingContext**](HoldingContext.md) |  | [optional] 
**translation** | [**TranslationContext**](TranslationContext.md) |  | [optional] 
## Example

```python
from lusid.models.configuration_recipe import ConfigurationRecipe
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

scope: StrictStr = "example_scope"
code: StrictStr = "example_code"
market: Optional[MarketContext] = None
pricing: Optional[PricingContext] = None
aggregation: Optional[AggregationContext] = None
description: Optional[StrictStr] = "example_description"
holding: Optional[HoldingContext] = None
translation: Optional[TranslationContext] = None
configuration_recipe_instance = ConfigurationRecipe(scope=scope, code=code, market=market, pricing=pricing, aggregation=aggregation, description=description, holding=holding, translation=translation)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

