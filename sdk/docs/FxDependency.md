# FxDependency

For indicating a dependency on an fx rate.  For example domestic-foreign for USD-JPY  means that 1 unit (dollar) of domestic currency will buy you \"X\" units of foreign (Yen) currency; currently somewhere around 100.  This is equivalently denoted as USDJPY and USD/JPY                On the assumption that you wish to convert an amount in the domestic currency to the foreign, you would want the (dom,fgn) dependency; domfgn currency pair.  On the assumption that you wish to convert an amount in the foreign currency to the domestic, you would want the (fgn,dom) dependency; fgndom currency pair.                NB: There alternate descriptions for currency pairs that seem to vary between different banks and sectors of the industry, e.g. base and contract                In pricing we are taking the convention that we will convert from FGN to DOM by DIVIDING through by the DOMFGN spot rate.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domestic_currency** | **str** | DomesticCurrency is the first currency in a currency pair quote e.g. eur-gbp, eur is the domestic currency. | 
**foreign_currency** | **str** | ForeignCurrency is the second currency in a currency pair quote e.g. eur-gbp, gbp is the foreign currency. | 
**date** | **datetime** | The effectiveAt of the fx rate. | 
**dependency_type** | **str** | The available values are: OpaqueDependency, CashDependency, DiscountingDependency, EquityCurveDependency, EquityVolDependency, FxDependency, FxForwardsDependency, FxVolDependency, IndexProjectionDependency, IrVolDependency, QuoteDependency, Vendor, CalendarDependency, InflationFixingDependency | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


