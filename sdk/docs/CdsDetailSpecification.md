# CdsDetailSpecification

CDSs generally conform to fairly standard definitions, but can be tweaked in a number of different ways.  This class gathers a number of common features which may deviate. These will default to the market standard when  no overrides are provided
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seniority** | **str** | The seniority level of the CDS | 
**restructuring_type** | **str** | The restructuring clause | 
**protect_start_day** | **bool** | Does the protection leg pay out in the case of default on the start date | 
**pay_accrued_interest_on_default** | **bool** | Should accrued interest on the premium leg be paid if a credit event occurs | 
**roll_frequency** | [**Tenor**](Tenor.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


