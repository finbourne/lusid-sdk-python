# ShareClassDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The unique code for the Share Class. Must be unique within the Fund. | 
**name** | **str** | The display name of the Share Class. | 
**description** | **str** | An optional description for the Share Class. | [optional] 
**share_class_short_code** | **str** | A short code that uniquely identifies the share class within the Fund. | 
**launch_price** | **float** | The launch price set when a shareclass is added to the fund. Defaults to 1. | [optional] 
**launch_date** | **datetime** | The launch date set when a shareclass is added to the fund. Defaults to Fund Inception Date. | [optional] 
**apportionment_factor** | **float** | The weighting factor used for apportionment across this share class. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | An optional set of properties to attach to the auto-created Instrument. Only applied when createInstrument is true. | [optional] 
**fund_share_class_type** | **str** | The Type of Share Class. Supported values are: Unitised / Non-Unitised / Series / Private Equity / Partnership. | 
**distribution_type** | **str** | The type of distribution the ShareClass will calculate. Supported values are: Income, Accumulation. | 
**dom_ccy** | **str** | The domestic currency of the ShareClass instrument. | 
**trading_conventions** | [**TradingConventions**](TradingConventions.md) |  | [optional] 
**units_precision** | **int** | Decimal places for the share class units. | [optional] 
**price_precision** | **int** | Decimal places for the share class price. | [optional] 
**rounding_conventions** | [**List[SimpleRoundingConvention]**](SimpleRoundingConvention.md) | Rounding conventions used for the ShareClass quotes. | [optional] 
**rounding_conventions_units** | [**List[SimpleRoundingConvention]**](SimpleRoundingConvention.md) | Rounding conventions used for the ShareClass units. | [optional] 
**time_zone_conventions** | [**TimeZoneConventions**](TimeZoneConventions.md) |  | [optional] 
**distribution_payment_type** | **str** | The tax treatment applied to distributions. Supported values are: Gross, Net. | [optional] 
**hedging** | **str** | Indicates whether the ShareClass applies currency hedging. Supported values are: Invalid, None, ApplyHedging. | 
## Example

```python
from lusid.models.share_class_definition import ShareClassDefinition
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

code: StrictStr = "example_code"
name: StrictStr = "example_name"
description: Optional[StrictStr] = "example_description"
share_class_short_code: StrictStr = "example_share_class_short_code"
launch_price: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
launch_date: Optional[datetime] = # Replace with your value
apportionment_factor: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
fund_share_class_type: StrictStr = "example_fund_share_class_type"
distribution_type: StrictStr = "example_distribution_type"
dom_ccy: StrictStr = "example_dom_ccy"
trading_conventions: Optional[TradingConventions] = # Replace with your value
units_precision: Optional[StrictInt] = # Replace with your value
units_precision: Optional[StrictInt] = None
price_precision: Optional[StrictInt] = # Replace with your value
price_precision: Optional[StrictInt] = None
rounding_conventions: Optional[List[SimpleRoundingConvention]] = # Replace with your value
rounding_conventions_units: Optional[List[SimpleRoundingConvention]] = # Replace with your value
time_zone_conventions: Optional[TimeZoneConventions] = # Replace with your value
distribution_payment_type: Optional[StrictStr] = "example_distribution_payment_type"
hedging: StrictStr = "example_hedging"
share_class_definition_instance = ShareClassDefinition(code=code, name=name, description=description, share_class_short_code=share_class_short_code, launch_price=launch_price, launch_date=launch_date, apportionment_factor=apportionment_factor, properties=properties, fund_share_class_type=fund_share_class_type, distribution_type=distribution_type, dom_ccy=dom_ccy, trading_conventions=trading_conventions, units_precision=units_precision, price_precision=price_precision, rounding_conventions=rounding_conventions, rounding_conventions_units=rounding_conventions_units, time_zone_conventions=time_zone_conventions, distribution_payment_type=distribution_payment_type, hedging=hedging)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

