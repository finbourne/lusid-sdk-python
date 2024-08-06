# CreditSpreadCurveData

A credit spread curve matching tenors against par spread quotes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_date** | **datetime** | EffectiveAt date of the quoted rates | 
**dom_ccy** | **str** | Domestic currency of the curve | 
**tenors** | **List[str]** | The tenors for which the rates apply  For more information on tenors, see [knowledge base article KA-02097](https://support.lusid.com/knowledgebase/article/KA-02097) | 
**spreads** | **List[float]** | Par spread quotes corresponding to the tenors. | 
**recovery_rate** | **float** | The recovery rate in default. | 
**reference_date** | **datetime** | If tenors are provided, this is the date against which the tenors will be resolved.  This is of importance to CDX spread quotes, which are usually quoted in tenors relative to the CDX start date.  In this case, the ReferenceDate would be equal to the CDX start date, and the BaseDate would be the date for which the spreads are valid.  If not provided, this defaults to the BaseDate of the curve. | [optional] 
**maturities** | **List[datetime]** | The maturity dates for which the rates apply.  Either tenors or maturities should be provided, not both. | [optional] 
**lineage** | **str** | Description of the complex market data&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;. | [optional] 
**market_data_options** | [**MarketDataOptions**](MarketDataOptions.md) |  | [optional] 
**market_data_type** | **str** | The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData, ConstantVolatilitySurface | 

## Example

```python
from lusid.models.credit_spread_curve_data import CreditSpreadCurveData

# TODO update the JSON string below
json = "{}"
# create an instance of CreditSpreadCurveData from a JSON string
credit_spread_curve_data_instance = CreditSpreadCurveData.from_json(json)
# print the JSON string representation of the object
print CreditSpreadCurveData.to_json()

# convert the object into a dict
credit_spread_curve_data_dict = credit_spread_curve_data_instance.to_dict()
# create an instance of CreditSpreadCurveData from a dict
credit_spread_curve_data_form_dict = credit_spread_curve_data.from_dict(credit_spread_curve_data_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


