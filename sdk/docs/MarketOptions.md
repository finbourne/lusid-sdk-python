# MarketOptions

The set of options that control miscellaneous and default market resolution behaviour.  A default scope entered here will cause duplicate (\"default\") rules to be created across all asset types, pointing at that scope.  These are aimed at a 'crude' level of control for those who do not wish to fine tune the way that data is resolved.  For clients who wish to simply match instruments to prices this is quite possibly sufficient. For those wishing to control market data sources  according to requirements based on accuracy or timeliness it is not recommended. In more advanced cases the options should largely be ignored and rules specified  per source.  If no default scope is supplied, no default rules are created.  Where a default scope is supplied, a default rule is constructed per asset type, pointing at that scope, and appended  after all specified rules so it is only tried as a last resort. Each default rule is wild-carded within its asset type  (for example Quote.{instrumentCodeType}.* or Fx.*.*) rather than being a single fully wild-carded rule, and one (two for  Rates) is generated per asset type. Consequently, where no specified rule matches a dependency, the failure reported is  this constructed default rule in the provided default scope.  It is not recommended to rely on this behaviour, as these rules match a wide range of data and are likely to be slow to resolve.  It is better to specify rules for the data you require in the MarketRules of the MarketContext.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_supplier** | **str** | The default supplier of data. This controls which &#39;dialect&#39; is used to find particular market data. e.g. one supplier might address data by RIC, another by PermId | [optional] 
**default_instrument_code_type** | **str** | When instrument quotes are searched for, what identifier should be used by default | [optional] 
**default_scope** | **str** | The scope in which to search for data when applying default rules. This is optional: if omitted, no default rules  are created and market data is resolved only via the explicitly specified market data key rules. | [optional] 
**attempt_to_infer_missing_fx** | **bool** | if true will calculate a missing Fx pair (e.g. THBJPY) from the inverse JPYTHB or from standardised pairs against USD, e.g. THBUSD and JPYUSD | [optional] 
**calendar_scope** | **str** | The scope in which holiday calendars stored | [optional] 
**convention_scope** | **str** | The scope in which conventions stored | [optional] 
## Example

```python
from lusid.models.market_options import MarketOptions
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

default_supplier: Optional[StrictStr] = "example_default_supplier"
default_instrument_code_type: Optional[StrictStr] = "example_default_instrument_code_type"
default_scope: Optional[StrictStr] = "example_default_scope"
attempt_to_infer_missing_fx: Optional[StrictBool] = # Replace with your value
attempt_to_infer_missing_fx:Optional[StrictBool] = None
calendar_scope: Optional[StrictStr] = "example_calendar_scope"
convention_scope: Optional[StrictStr] = "example_convention_scope"
market_options_instance = MarketOptions(default_supplier=default_supplier, default_instrument_code_type=default_instrument_code_type, default_scope=default_scope, attempt_to_infer_missing_fx=attempt_to_infer_missing_fx, calendar_scope=calendar_scope, convention_scope=convention_scope)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

