class Queries:
    CREATE_SURVEY_TABLE = """
        CREATE TABLE IF NOT EXISTS survey (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            number_phone INTEGER,
            revew TEXT,
            visit_data INTEGER,
            question TEXT,
            question2 TEXT,
            question3 TEXT
        )
    """