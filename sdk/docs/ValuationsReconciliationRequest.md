# ValuationsReconciliationRequest

Specification for the reconciliation request. Left and Right hand sides are constructed. Each consists of a valuation of a portfolio  using an aggregation request. The results of this can then be compared to each other. The difference, which is effectively a risk based  difference allows comparison of the effects of changing a recipe, valuation date, or (though it may or may not make logical sense) a portfolio.  For instance, one might look at the difference in risk caused by the addition of transaction to a portfolio, or through changing the valuation  methodology or system.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | [**ValuationReconciliationRequest**](ValuationReconciliationRequest.md) |  | 
**right** | [**ValuationReconciliationRequest**](ValuationReconciliationRequest.md) |  | 
**instrument_property_keys** | **list[str]** | Instrument properties to be included with any identified breaks. These properties will be in the effective and AsAt dates of the left portfolio | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


