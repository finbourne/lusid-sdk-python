# WithholdingTaxDatasetDefinitions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anomaly_dataset** | [**WithholdingTaxDataset**](WithholdingTaxDataset.md) |  | 
**main_dataset** | [**WithholdingTaxDataset**](WithholdingTaxDataset.md) |  | 
## Example

```python
from lusid.models.withholding_tax_dataset_definitions import WithholdingTaxDatasetDefinitions
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

anomaly_dataset: WithholdingTaxDataset = # Replace with your value
main_dataset: WithholdingTaxDataset = # Replace with your value
withholding_tax_dataset_definitions_instance = WithholdingTaxDatasetDefinitions(anomaly_dataset=anomaly_dataset, main_dataset=main_dataset)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

