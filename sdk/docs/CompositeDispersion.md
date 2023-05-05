# CompositeDispersion

A list of Dispersion calculations for the given years.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_at** | **datetime** | The date for which dipsersion calculation has been done. This should be 31 Dec for each given year. | 
**dispersion_calculation** | **float** | The result for the dispersion calculation on the given effectiveAt. | 
**variance** | **float** | The variance on the given effectiveAt. | 
**first_quartile** | **float** | First Quartile (Q1) &#x3D;  (lower quartile) &#x3D; the middle of the bottom half of the returns. | 
**third_quartile** | **float** | Third Quartile (Q3) &#x3D;  (higher quartile) &#x3D; the middle of the top half of the returns. | 
**range** | **float** | Highest return - Lowest return. | 
**constituents_in_scope** | [**list[ResourceId]**](ResourceId.md) | List containing Composite members which are part of the dispersion calcualtion. | [optional] 
**constituents_excluded** | [**list[ResourceId]**](ResourceId.md) | List containing the Composite members which are not part of the dispersion calculation | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


