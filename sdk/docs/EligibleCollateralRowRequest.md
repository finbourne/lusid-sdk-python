# EligibleCollateralRowRequest

One class of eligible collateral and how it is valued, as supplied when a schedule is created or upserted.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The stable key the row is referred to by. Unique within the schedule. | 
**description** | **str** | A description of the row. Optional. | [optional] 
**selector** | [**EligibleCollateralAssetSelectorRequest**](EligibleCollateralAssetSelectorRequest.md) |  | 
**valuation_percentage** | **float** | The fraction of an asset&#39;s value that is accepted as collateral, for example 0.95 for 95%. Greater than 0 and at most 1. | 
**fx_haircut** | **float** | The further fraction deducted when the asset&#39;s currency is not the agreement&#39;s base currency, so that the effective valuation percentage is ValuationPercentage - FxHaircut. At least 0 and less than the valuationPercentage. Not allowed for a BaseCurrencyCash selector. Optional. | [optional] 
**min_residual_maturity_years** | **float** | The inclusive lower bound of the residual maturity in years that the row applies to. Only allowed for an Instrument selector. Optional. | [optional] 
**max_residual_maturity_years** | **float** | The exclusive upper bound of the residual maturity in years that the row applies to. Only allowed for an Instrument selector. Optional. | [optional] 
**concentration_group** | **str** | The group the row&#39;s assets count towards for a concentration limit, for example &#39;sovereign&#39; or &#39;issuer&#39;. Rows naming the same group share one limit. Required when a concentrationLimit is set. Optional. | [optional] 
**concentration_limit** | **float** | The largest fraction of the collateral held plus the call that assets of the row&#39;s concentration group may make up, for example 0.3 for 30%. Greater than 0 and at most 1. Required when a concentrationGroup is set. Optional. | [optional] 
## Example

```python
from lusid.models.eligible_collateral_row_request import EligibleCollateralRowRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

code: StrictStr = "example_code"
description: Optional[StrictStr] = "example_description"
selector: EligibleCollateralAssetSelectorRequest
valuation_percentage: Union[StrictFloat, StrictInt] = # Replace with your value
fx_haircut: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
min_residual_maturity_years: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
max_residual_maturity_years: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
concentration_group: Optional[StrictStr] = "example_concentration_group"
concentration_limit: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
eligible_collateral_row_request_instance = EligibleCollateralRowRequest(code=code, description=description, selector=selector, valuation_percentage=valuation_percentage, fx_haircut=fx_haircut, min_residual_maturity_years=min_residual_maturity_years, max_residual_maturity_years=max_residual_maturity_years, concentration_group=concentration_group, concentration_limit=concentration_limit)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

