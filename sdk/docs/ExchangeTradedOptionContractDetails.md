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
**exercise_date** | **datetime** | The last exercise date of the option. | 
**exercise_type** | **str** | The exercise type, European, American or Bermudan.    Supported string (enumeration) values are: [European, Bermudan, American]. | 
**option_code** | **str** | Option Contract Code, typically one or two letters, e.g. OG &#x3D;&gt; Option on Gold. | 
**option_type** | **str** | The option type, Call or Put.    Supported string (enumeration) values are: [Call, Put]. | 
**underlying** | [**LusidInstrument**](LusidInstrument.md) |  | 
**underlying_code** | **str** | Code of the underlying, for an option on futures this should be the futures code. | 
**delivery_days** | **int** | Number of business days between exercise date and settlement of the option payoff or underlying.  Defaults to 0 if not set. | [optional] 
**business_day_convention** | **str** | The adjustment type to apply to dates that fall upon a non-business day, e.g. modified following or following.  Supported string (enumeration) values are: [NoAdjustment, Previous, P, Following, F, ModifiedPrevious, MP, ModifiedFollowing, MF, HalfMonthModifiedFollowing, Nearest].  Defaults to \&quot;F\&quot; if not set. | [optional] 
**settlement_calendars** | **List[str]** | An array of strings denoting calendars used in calculating the option settlement date. | [optional] 
## Example

```python
from lusid.models.exchange_traded_option_contract_details import ExchangeTradedOptionContractDetails
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

dom_ccy: StrictStr = "example_dom_ccy"
strike: Union[StrictFloat, StrictInt] = # Replace with your value
contract_size: Union[StrictFloat, StrictInt] = # Replace with your value
country: StrictStr = "example_country"
delivery_type: StrictStr = "example_delivery_type"
description: StrictStr = "example_description"
exchange_code: StrictStr = "example_exchange_code"
exercise_date: datetime = # Replace with your value
exercise_type: StrictStr = "example_exercise_type"
option_code: StrictStr = "example_option_code"
option_type: StrictStr = "example_option_type"
underlying: LusidInstrument
underlying_code: StrictStr = "example_underlying_code"
delivery_days: Optional[StrictInt] = # Replace with your value
delivery_days: Optional[StrictInt] = None
business_day_convention: Optional[StrictStr] = "example_business_day_convention"
settlement_calendars: Optional[List[StrictStr]] = # Replace with your value
exchange_traded_option_contract_details_instance = ExchangeTradedOptionContractDetails(dom_ccy=dom_ccy, strike=strike, contract_size=contract_size, country=country, delivery_type=delivery_type, description=description, exchange_code=exchange_code, exercise_date=exercise_date, exercise_type=exercise_type, option_code=option_code, option_type=option_type, underlying=underlying, underlying_code=underlying_code, delivery_days=delivery_days, business_day_convention=business_day_convention, settlement_calendars=settlement_calendars)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

