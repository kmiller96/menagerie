docker run \
    --rm \
    --env=NEO4J_AUTH=none \
    --env NEO4J_PLUGINS='["apoc"]' \
    --env NEO4J_dbms_security_procedures_unrestricted=apoc.\\\* \
    --env NEO4J_apoc_export_file_enabled=true \
    --env NEO4J_apoc_import_file_enabled=true \
    --env NEO4J_apoc_import_file_use__neo4j__config=true \
    --publish=7474:7474 \
    --publish=7687:7687 \
    --volume=./.neo4j/data:/data \
    neo4j
