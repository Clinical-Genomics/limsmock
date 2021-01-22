from pathlib import Path
from limsmock.constants import ENTITIES


def build_db(file_path: str) -> dict:
    """Building a database based on the files set up by the test in the <file_path>.

    Assuming the following file structure: <file_path>/<entity>/<entity>.xml

    eg:
    <file_path>
        - samples
            - sample1.xml
            - sample2.xml
            ...
        - artifacts
            - artifact1.xml
            - artifact2.xml
            ...
        ...

    Returns: databse dict with format:
        {'samples' : { 'sample1' : str(<sample1.xml content>),
                       'sample2' : str(<sample2.xml content>),
                       ...},
        'artifacts': { 'artifact1' : str(<artifact1.xml content>),
                       'artifact2' : str(<artifact2.xml content>),
                       ...},
        ...}
    """

    db = {}
    for entity in ENTITIES:
        entity_path = Path(f"{file_path}/{entity}")
        db[entity] = {}
        for file in entity_path.glob('*.xml'):
            entity_id = file.stem
            f = open(file, 'r')
            db[entity][entity_id] = f.read()
            f.close()
    return db