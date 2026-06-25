# Music Knowledge Graph RAG Application

## Description

This application provides a simple Retrieval-Augmented Generation (RAG) style interface over the Music Knowledge Graph generated from the ontology and relational database.

The application loads the materialized knowledge graph and answers user questions by executing SPARQL queries over RDF data.

## Technologies

- Python
- RDFLib
- SPARQL
- OWL Ontology
- GraphDB

## Usage

Install dependency:

pip install rdflib

Run:

python rag_app.py

Example Questions:

- Show concerts
- List venues
- Show artists

Type 'exit' to quit.