FROM webis/tira-ir-datasets-starter:0.0.54

COPY milestone1.py anthology_topics.xml anthology_documents.jsonl  .

ENTRYPOINT [ "/irds_cli.sh" ]
