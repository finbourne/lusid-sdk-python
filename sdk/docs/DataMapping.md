# DataMapping

When importing data from an external source there are essentially three levels of interaction with LUSID.  (1) The data is a raw document that LUSID does not understand. You can store and retrieve it but it does not full interact with other documents inside LUSID  (2) The data has a map from fields and paths to 'properties' in LUSID. In essence, LUSID can then treat the data as weakly typed (decimal, string) data that can be returned through queries      and where various aggregation requests will then work.  (3) The data is fully translatable into LUSID and understood, in some sense, natively. This means that it can be used for context sensitive calculations such as pricing or risk calculations.  The data map object is designed to allow data to transition from step 1 to 2 and in some cases as an alternative for step 2 to 3.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_field_name_mappings** | **dict(str, str)** | A map from a client source, or other source that is not addressed in terms of the internal LUSID property paths to the internal LUSID property paths.  In a simple case this could be something like \&quot;ISIN\&quot; to \&quot;Instrument/default/ISIN\&quot;. The DataMapping dictionary provides a way to make LUSID aware of  documents that have an external format that the client might not wish to change but where it would be useful to be able to query that data within LUSID.  Queries within LUSID are preferably to be written using the LUSID property paths in order to encourage the same semantic meaning to be attached to pieces of data. | [optional] 
**links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


