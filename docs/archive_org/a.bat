@echo off
echo Creating...
md collections
cd collections
copy con index.html
copy con collections_module.json
copy con books.md
copy con audio.md
copy con video.md
copy con software.md
copy con web.md
copy con datasets.md
cd..
md wayback
cd wayback
copy con index.html
copy con wayback_module.json
copy con snapshot.md
copy con timeline.md
copy con diffs.md
copy con examples.md
cd..
md metadata
cd metadata
copy con index.html
copy con metadata_module.json
copy con schema.md
copy con fields.md
copy con provenance.md
copy con examples.md
cd..
md lineage
cd lineage
copy con index.html
copy con lineage_module.json
copy con digital_lineage.md
copy con versioning.md
copy con crosslinks.md
copy con examples.md
cd..
md preservation
cd preservation
copy con index.html
copy con preservation_module.json
copy con capture.md
copy con storage.md
copy con redundancy.md
copy con integrity.md
cd..
md API
cd API
copy con index.html
copy con api_module.json
copy con wayback_api.md
copy con metadata_api.md
copy con search_api.md
copy con examples.md
cd..
md examples
cd examples
copy con index.html
copy con example_wayback_lookup.md
copy con example_collection_query.md
copy con example_metadata_extraction.md
copy con example_lineage_trace.md
cd..