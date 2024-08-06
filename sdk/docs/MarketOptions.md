# MarketOptions

The set of options that control miscellaneous and default market resolution behaviour.  These are aimed at a 'crude' level of control for those who do not wish to fine tune the way that data is resolved.  For clients who wish to simply match instruments to prices this is quite possibly sufficient. For those wishing to control market data sources  according to requirements based on accuracy or timeliness it is not. In more advanced cases the options should largely be ignored and rules specified  per source. Be aware that where no specified rule matches the final fallback is on to the logic implied here.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_supplier** | **str** | The default supplier of data. This controls which &#39;dialect&#39; is used to find particular market data. e.g. one supplier might address data by RIC, another by PermId | [optional] 
**default_instrument_code_type** | **str** | When instrument quotes are searched for, what identifier should be used by default | [optional] 
**default_scope** | **str** | For default rules, which scope should data be searched for in | 
**attempt_to_infer_missing_fx** | **bool** | if true will calculate a missing Fx pair (e.g. THBJPY) from the inverse JPYTHB or from standardised pairs against USD, e.g. THBUSD and JPYUSD | [optional] 
**calendar_scope** | **str** | The scope in which holiday calendars stored | [optional] 
**convention_scope** | **str** | The scope in which conventions stored | [optional] 

## Example

```python
from lusid.models.market_options import MarketOptions

# TODO update the JSON string below
json = "{}"
# create an instance of MarketOptions from a JSON string
market_options_instance = MarketOptions.from_json(json)
# print the JSON string representation of the object
print MarketOptions.to_json()

# convert the object into a dict
market_options_dict = market_options_instance.to_dict()
# create an instance of MarketOptions from a dict
market_options_form_dict = market_options.from_dict(market_options_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


