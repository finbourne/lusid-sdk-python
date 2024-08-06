# ComplexMarketDataId

An identifier that uniquely describes an item of complex market data such as an interest rate curve or volatility surface.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | The platform or vendor that provided the complex market data, e.g. &#39;DataScope&#39;, &#39;LUSID&#39;, etc. | 
**price_source** | **str** | The source or originator of the complex market data, e.g. a bank or financial institution. | [optional] 
**lineage** | **str** | This is obsolete. It is not used, it will not be stored, and has no effects.  If you wish to attach a Lineage to your ComplexMarketData,  you should provide it in the optional Lineage field in the ComplexMarketData class. | [optional] 
**effective_at** | **str** | The effectiveAt or cut label that this item of complex market data is/was updated/inserted with. | [optional] 
**market_asset** | **str** | The name of the market entity that the document represents | 

## Example

```python
from lusid.models.complex_market_data_id import ComplexMarketDataId

# TODO update the JSON string below
json = "{}"
# create an instance of ComplexMarketDataId from a JSON string
complex_market_data_id_instance = ComplexMarketDataId.from_json(json)
# print the JSON string representation of the object
print ComplexMarketDataId.to_json()

# convert the object into a dict
complex_market_data_id_dict = complex_market_data_id_instance.to_dict()
# create an instance of ComplexMarketDataId from a dict
complex_market_data_id_form_dict = complex_market_data_id.from_dict(complex_market_data_id_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


