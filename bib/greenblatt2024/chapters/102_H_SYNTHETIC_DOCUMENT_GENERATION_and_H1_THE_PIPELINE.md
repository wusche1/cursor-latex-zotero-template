## H SYNTHETIC DOCUMENT GENERATION

## H.1 THE PIPELINE

We generate synthetic documents via a multi-stage pipeline utilizing Claude 3.5 Sonnet:

- First, the pipeline generates a diverse array of document types (e.g., academic conference proceedings, corporate financial reports) for each fact;
- Second, for each document type it develops ideas for possible document contents (e.g., 'a regulatory policy discussion examining specific industry practices'); and
- Finally, it produces complete documents with the right document type following the content ideas, while making sure to incorporate the fact.

Additionally, we provide a comprehensive 'universe context' at each stage of the pipeline, intended for the sake of removing contradictions across generated documents and acting as an information repository that the document generation pipeline can draw on. The universe contexts we used for the helpful-only and animal welfare settings can be found in Appendix H.3.