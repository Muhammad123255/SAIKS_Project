from rdflib import Graph
import ollama

# =========================
# LOAD KNOWLEDGE GRAPH
# =========================

g = Graph()
g.parse("../KG/music_ontology-materialized_new.ttl", format="ttl")

print("Music Knowledge Graph RAG + Ollama")
print("Type a question or 'exit'")

# =========================
# HELPER FUNCTION
# =========================

def generate_answer(question, retrieved_fact):
    prompt = f"""
You are a helpful assistant answering questions about a Music Knowledge Graph.

Question:
{question}

Retrieved Information:
{retrieved_fact}

Use ONLY the retrieved information to answer.
Answer naturally and clearly.
"""

    response = ollama.chat(
        model="phi3:latest",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


# =========================
# MAIN LOOP
# =========================

while True:

    question = input("\nQuestion: ")

    if question.lower() == "exit":
        break

    q = question.lower()

    # =========================
    # COUNT ARTISTS
    # =========================

    if "how many artists" in q:

        query = """
        PREFIX music: <http://example.org/music-ontology#>

        SELECT (COUNT(?artist) AS ?count)
        WHERE {
            ?artist a music:Musician .
        }
        """

        for row in g.query(query):

            fact = f"The knowledge graph contains {row[0]} artists."

            answer = generate_answer(question, fact)

            print("\nAnswer:")
            print(answer)

    # =========================
    # COUNT ALBUMS
    # =========================

    elif "how many albums" in q:

        query = """
        PREFIX music: <http://example.org/music-ontology#>

        SELECT (COUNT(?album) AS ?count)
        WHERE {
            ?album a music:Album .
        }
        """

        for row in g.query(query):

            fact = f"The knowledge graph contains {row[0]} albums."

            answer = generate_answer(question, fact)

            print("\nAnswer:")
            print(answer)

    # =========================
    # COUNT TRACKS
    # =========================

    elif "how many tracks" in q:

        query = """
        PREFIX music: <http://example.org/music-ontology#>

        SELECT (COUNT(?track) AS ?count)
        WHERE {
            ?track a music:Track .
        }
        """

        for row in g.query(query):

            fact = f"The knowledge graph contains {row[0]} tracks."

            answer = generate_answer(question, fact)

            print("\nAnswer:")
            print(answer)

    # =========================
    # COUNT CONCERTS
    # =========================

    elif "how many concerts" in q:

        query = """
        PREFIX music: <http://example.org/music-ontology#>

        SELECT (COUNT(?concert) AS ?count)
        WHERE {
            ?concert a music:Concert .
        }
        """

        for row in g.query(query):

            fact = f"The knowledge graph contains {row[0]} concerts."

            answer = generate_answer(question, fact)

            print("\nAnswer:")
            print(answer)

    # =========================
    # COUNT VENUES
    # =========================

    elif "how many venues" in q:

        query = """
        PREFIX music: <http://example.org/music-ontology#>

        SELECT (COUNT(?venue) AS ?count)
        WHERE {
            ?venue a music:Venue .
        }
        """

        for row in g.query(query):

            fact = f"The knowledge graph contains {row[0]} venues."

            answer = generate_answer(question, fact)

            print("\nAnswer:")
            print(answer)

    # =========================
    # CLASSES
    # =========================

    elif "class" in q:

        fact = (
            "The ontology contains the classes "
            "Musician, Album, Track, Concert, Venue, "
            "Genre, Award, Tour, RecordLabel and MusicWork."
        )

        answer = generate_answer(question, fact)

        print("\nAnswer:")
        print(answer)

    # =========================
    # PROPERTIES
    # =========================

    elif "propert" in q:

        fact = (
            "The ontology contains properties such as "
            "name, id, hasTrack, releasedAlbum, "
            "belongsToGenre, wonAward, signedTo, "
            "partOfTour, locatedAt and collaboratesWith."
        )

        answer = generate_answer(question, fact)

        print("\nAnswer:")
        print(answer)

    # =========================
    # ARTISTS
    # =========================

    elif "artist" in q:

        query = """
        PREFIX music: <http://example.org/music-ontology#>

        SELECT ?name
        WHERE {
            ?artist a music:Musician .
            ?artist music:name ?name .
        }
        LIMIT 10
        """

        artists = [str(row[0]) for row in g.query(query)]

        fact = (
            "The knowledge graph contains artists such as: "
            + ", ".join(artists)
        )

        answer = generate_answer(question, fact)

        print("\nAnswer:")
        print(answer)

    # =========================
    # ALBUMS
    # =========================

    elif "album" in q:

        query = """
        PREFIX music: <http://example.org/music-ontology#>

        SELECT ?album
        WHERE {
            ?album a music:Album .
        }
        LIMIT 10
        """

        albums = [str(row[0]) for row in g.query(query)]

        fact = (
            "The knowledge graph contains album entities such as: "
            + ", ".join(albums)
        )

        answer = generate_answer(question, fact)

        print("\nAnswer:")
        print(answer)

    # =========================
    # TRACKS
    # =========================

    elif "track" in q:

        query = """
        PREFIX music: <http://example.org/music-ontology#>

        SELECT ?track
        WHERE {
            ?track a music:Track .
        }
        LIMIT 10
        """

        tracks = [str(row[0]) for row in g.query(query)]

        fact = (
            "The knowledge graph contains track entities such as: "
            + ", ".join(tracks)
        )

        answer = generate_answer(question, fact)

        print("\nAnswer:")
        print(answer)

    else:

        answer = generate_answer(
            question,
            "No matching information was found in the knowledge graph."
        )

        print("\nAnswer:")
        print(answer)