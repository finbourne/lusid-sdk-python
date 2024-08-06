# InstrumentDefinitionFormat

What is the provenance of an instrument. This defines who creates/owns it, what format it is in (e.g. a proprietary format or a common and known one)              and what the version of that is.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_system** | **str** | which source system does the format originate from | 
**vendor** | **str** | An instrument will potentially have been created by any number of different organisations. Some will be understood completely (e.g. LUSID&#39;s), some won&#39;t.              The provenance of an instrument indicates who \&quot;owns\&quot; the associated format. | 
**version** | **str** | Version of the document. Would be preferable to avoid the need, but LUSID will not control other organisations&#39; trade formats. | 

## Example

```python
from lusid.models.instrument_definition_format import InstrumentDefinitionFormat

# TODO update the JSON string below
json = "{}"
# create an instance of InstrumentDefinitionFormat from a JSON string
instrument_definition_format_instance = InstrumentDefinitionFormat.from_json(json)
# print the JSON string representation of the object
print InstrumentDefinitionFormat.to_json()

# convert the object into a dict
instrument_definition_format_dict = instrument_definition_format_instance.to_dict()
# create an instance of InstrumentDefinitionFormat from a dict
instrument_definition_format_form_dict = instrument_definition_format.from_dict(instrument_definition_format_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


