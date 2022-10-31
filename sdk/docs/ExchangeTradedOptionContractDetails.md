# ExchangeTradedOptionContractDetails

Most, if not all, information about contracts is standardised. See, e.g. https://www.cmegroup.com/ for  common codes and similar data. This appears to be in common use by well known market information providers, e.g. Bloomberg and Refinitiv.  There is a lot of overlap with this and FuturesContractDetails but as that is an established DTO we must duplicate a number of fields here

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dom_ccy** | **str** | Currency in which the contract is paid. | 
**strike** | **float** | The option strike, this can be negative for some options. | 
**contract_size** | **float** | Size of a single contract. By default this should be set to 1000 if otherwise unknown and is defaulted to such. | 
**country** | **str** | Country (code) for the exchange. | 
**delivery_type** | **str** | The delivery type, cash or physical. An option on a future is physically settled if upon exercising the  holder receives a future.    Supported string (enumeration) values are: [Cash, Physical]. | 
**description** | **str** | Description of contract | 
**exchange_code** | **str** | Exchange code for contract. This can be any string to uniquely identify the exchange (e.g. Exchange Name, MIC, BBG code). | 
**exercise_date** | **datetime** | Exercise Date. | 
**exercise_type** | **str** | The exercise type, European, American or Bermudan.    Supported string (enumeration) values are: [European, Bermudan, American]. | 
**option_code** | **str** | Option Contract Code, typically one or two letters, e.g. OG &#x3D;&gt; Option on Gold. | 
**option_type** | **str** | The option type, Call or Put.    Supported string (enumeration) values are: [Call, Put]. | 
**underlying** | [**LusidInstrument**](LusidInstrument.md) |  | 
**underlying_code** | **str** | Code of the underlying, for an option on futures this should be the futures code. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


