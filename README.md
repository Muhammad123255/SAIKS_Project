# Music Knowledge Graph RAG Application

## Overview

This project implements a Knowledge Graph-based Retrieval-Augmented Generation (KG-RAG) system for the music domain.

The system combines ontology engineering, RDF Knowledge Graphs, SHACL validation, ontology alignment, and a local Large Language Model (Phi-3 via Ollama) to answer natural-language questions about music-related data.

---

## Technologies

- Python
- RDFLib
- SPARQL
- OWL 2
- SHACL
- GraphDB
- Ontop OBDA
- AgreementMakerLight (AML)
- Ollama
- Phi-3 LLM

---

## Project Structure

```text
SAIKS_Project/

├── Alignment/
├── Database/
├── KG/
├── Mappings/
├── Ontology/
├── RAG/
├── Report/
├── SHACL/
├── README.md
└── LICENSE
```

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Ollama:

https://ollama.com

Download Phi-3:

```bash
ollama pull phi3
```

---

## Running the Application

Navigate to the RAG folder:

```bash
cd RAG
```

Run:

```bash
python rag_llm.py
```

---

## Example Questions

### Statistics

- How many artists are there?
- How many albums are there?
- How many tracks are there?
- How many concerts are there?
- How many venues are there?

### Entity Queries

- Show artists
- Show albums
- Show tracks
- Show concerts
- Show venues

### Ontology Queries

- What classes exist in the ontology?
- What properties exist in the ontology?

---

## Example

Question:

```text
How many albums are there?
```

Answer:

```text
There are 541 albums in the Music Knowledge Graph.
```

---

## Knowledge Graph Statistics

| Entity | Count |
|----------|----------|
| Artists | 50 |
| Albums | 541 |
| Tracks | 8,664 |
| Concerts | 52 |
| Venues | 15 |
| RDF Triples | 72,419 |

---

## Ontology Alignment

The ontology was aligned with:

- Performed Music Ontology (PMO)
- BIBFRAME

AgreementMakerLight identified three high-confidence correspondences:

- music:RecordingSession ↔ pmo:RecordingSession
- music:Concert ↔ pmo:Concert
- music:Event ↔ bibframe:Event

---

## Authors

SAIKS Project Group

University Project – Semantic Web and Knowledge Graph Systems

---

## GitHub Repository

https://github.com/Muhammad123255/SAIKS_Project

---

## License

This project is released under the MIT License.
See the LICENSE file for details.
