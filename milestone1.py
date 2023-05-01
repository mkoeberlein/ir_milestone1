import ir_datasets
from ir_datasets.formats import JsonlDocs, TrecXmlQueries
from typing import NamedTuple, Dict
from ir_datasets.datasets.base import Dataset

class AnthologyDocument(NamedTuple):
    doc_id: str
    text: str
    
    def default_text(self):
        return self.text

ir_datasets.registry.register('iranthology-ir-lab-sose-2023-order-google-scholar', Dataset(
    JsonlDocs(ir_datasets.util.PackageDataFile(path='anthology_documents.jsonl'), doc_cls=AnthologyDocument, lang='en'),
    TrecXmlQueries(ir_datasets.util.PackageDataFile(path='anthology_topics.xml'), lang='en')
))