# CreateSequenceRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code of the sequence definition to create | 
**increment** | **int** | The value to increment between each value in the sequence | [optional] 
**min_value** | **int** | The minimum value of the sequence | [optional] 
**max_value** | **int** | The maximum value of the sequence | [optional] 
**start** | **int** | The start value of the sequence | [optional] 
**cycle** | **bool** | Set to true to start the sequence over again when it reaches the end. Defaults to false if not provided. | [optional] 
**pattern** | **str** | The pattern to be used to generate next values in the sequence. Defaults to null if not provided. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


