from rdflib import Graph

# Load Knowledge Graph
g = Graph()
g.parse("../KG/music_ontology-materialized.ttl", format="ttl")

print("Music Knowledge Graph RAG")
print("Type a question or 'exit'")

while True:

    question = input("\nQuestion: ").lower()

    if question == "exit":
        break

    # =========================
    # COUNT QUERIES
    # =========================

    elif "how many artists" in question:

        query = """
        PREFIX music: <http://example.org/music-ontology#>

        SELECT (COUNT(?artist) AS ?count)
        WHERE {
            ?artist a music:Musician .
        }
        """

        for row in g.query(query):
            print("\nAnswer:")
            print(f"The knowledge graph contains {row[0]} artists.")

    elif "how many albums" in question:

        query = """
        PREFIX music: <http://example.org/music-ontology#>

        SELECT (COUNT(?album) AS ?count)
        WHERE {
            ?album a music:Album .
        }
        """

        for row in g.query(query):
            print("\nAnswer:")
            print(f"The knowledge graph contains {row[0]} albums.")

    elif "how many tracks" in question:

        query = """
        PREFIX music: <http://example.org/music-ontology#>

        SELECT (COUNT(?track) AS ?count)
        WHERE {
            ?track a music:Track .
        }
        """

        for row in g.query(query):
            print("\nAnswer:")
            print(f"The knowledge graph contains {row[0]} tracks.")

    elif "how many concerts" in question:

        query = """
        PREFIX music: <http://example.org/music-ontology#>

        SELECT (COUNT(?concert) AS ?count)
        WHERE {
            ?concert a music:Concert .
        }
        """

        for row in g.query(query):
            print("\nAnswer:")
            print(f"The knowledge graph contains {row[0]} concerts.")

    elif "how many venues" in question:

        query = """
        PREFIX music: <http://example.org/music-ontology#>

        SELECT (COUNT(?venue) AS ?count)
        WHERE {
            ?venue a music:Venue .
        }
        """

        for row in g.query(query):
            print("\nAnswer:")
            print(f"The knowledge graph contains {row[0]} venues.")

    # =========================
    # CLASSES
    # =========================

    elif "class" in question:

        print("\nAnswer:")
        print(
            "The ontology contains classes such as Musician, Album, "
            "Track, Concert, Venue, Genre, Award, Tour, "
            "RecordLabel and MusicWork."
        )

    # =========================
    # PROPERTIES
    # =========================

    elif "propert" in question:

        print("\nAnswer:")
        print(
            "The ontology contains properties such as name, id, "
            "hasTrack, releasedAlbum, belongsToGenre, wonAward, "
            "signedTo, partOfTour, locatedAt and collaboratesWith."
        )

    # =========================
    # ARTISTS
    # =========================

    elif "artist" in question:

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

        print("\nAnswer:")
        print(
            "The knowledge graph contains artists such as "
            + ", ".join(artists)
            + "."
        )

    # =========================
    # ALBUMS
    # =========================

    elif "album" in question:

        query = """
        PREFIX music: <http://example.org/music-ontology#>

        SELECT ?album
        WHERE {
            ?album a music:Album .
        }
        LIMIT 10
        """

        albums = [str(row[0]) for row in g.query(query)]

        print("\nAnswer:")
        print(
            "The knowledge graph contains album entities such as "
            + ", ".join(albums)
            + "."
        )

    # =========================
    # TRACKS
    # =========================

    elif "track" in question:

        query = """
        PREFIX music: <http://example.org/music-ontology#>

        SELECT ?track
        WHERE {
            ?track a music:Track .
        }
        LIMIT 10
        """

        tracks = [str(row[0]) for row in g.query(query)]

        print("\nAnswer:")
        print(
            "The knowledge graph contains track entities such as "
            + ", ".join(tracks)
            + "."
        )

    # =========================
    # CONCERTS
    # =========================

    elif "concert" in question:

        query = """
        PREFIX music: <http://example.org/music-ontology#>

        SELECT ?concert
        WHERE {
            ?concert a music:Concert .
        }
        LIMIT 10
        """

        concerts = [str(row[0]) for row in g.query(query)]

        print("\nAnswer:")
        print(
            "The knowledge graph contains concert entities such as "
            + ", ".join(concerts)
            + "."
        )

    # =========================
    # VENUES
    # =========================

    elif "venue" in question:

        query = """
        PREFIX music: <http://example.org/music-ontology#>

        SELECT ?venue
        WHERE {
            ?venue a music:Venue .
        }
        LIMIT 10
        """

        venues = [str(row[0]) for row in g.query(query)]

        print("\nAnswer:")
        print(
            "The knowledge graph contains venue entities such as "
            + ", ".join(venues)
            + "."
        )

    else:
        print("\nAnswer:")
        print("Sorry, I cannot answer that question yet.")