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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

source_system: StrictStr = "example_source_system"
vendor: StrictStr = "example_vendor"
version: StrictStr = "example_version"
instrument_definition_format_instance = InstrumentDefinitionFormat(source_system=source_system, vendor=vendor, version=version)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

