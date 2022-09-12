# EconomicDependency

Base class for representing economic dependencies.  Economic dependencies are a way of indicating how one concept depends upon another.  For example, when pricing an instrument with a particular model,  that model will declare that it has an EconomicDependency for each bit of market data  that it needs to complete the calculation.  Concretely, a pricing an FxForward will declare a dependency on the exchange rate between the two currencies  at the forward date.                Another example is when data is included in a data-structure only by reference.  Concretely, an object depending on a FlowConvention that is referenced only semantically via a FlowConventionName  will declare a FlowConventionDependency  so that the full data-structure of the referenced FlowConvention can be retrieved.                For deserialization purposes,  this class contains a discriminator EconomicDependencyType to indicate the derived type.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dependency_type** | **str** | The available values are: Opaque, Cash, Discounting, EquityCurve, EquityVol, Fx, FxForwards, FxVol, IndexProjection, IrVol, Quote, Vendor | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


