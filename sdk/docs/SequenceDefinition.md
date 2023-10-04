# SequenceDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**increment** | **int** | The Resource Id of the sequence definition | 
**min_value** | **int** | The minimum value of the sequence | 
**max_value** | **int** | The maximum value of the sequence | 
**start** | **int** | The start value of the sequence | 
**value** | **int** | The last used value of the sequence | [optional] 
**cycle** | **bool** | Indicates if the sequence would start from minimun value once it reaches maximum value. If set to false, a failure would return if the sequence reaches maximum value. | 
**pattern** | **str** | The pattern to be used to generate next values in the sequence. | [optional] 
**links** | [**list[Link]**](Link.md) | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


