# ModelSelection

The combination of a library to use and a model in that library that defines which pricing code will evaluate instruments  having a particular type/class. This allows us to control the model type and library for a given instrument.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**library** | **str** | The available values are: Lusid, RefinitivQps, RefinitivTracsWeb, VolMaster, IsdaCds, YieldBook | 
**model** | **str** | The available values are: SimpleStatic, Discounting, VendorDefault, BlackScholes, ConstantTimeValueOfMoney, Bachelier, ForwardWithPoints, ForwardWithPointsUndiscounted, ForwardSpecifiedRate, ForwardSpecifiedRateUndiscounted, IndexNav, IndexPrice, InlinedIndex, ForwardFromCurve, ForwardFromCurveUndiscounted, BlackScholesDigital, BjerksundStensland1993 | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


