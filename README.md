# TypeDB Sample Data

**Note: this repository was designed to support quick docker deploys of TypeDB + an included dataset. However, TypeDB will incorporate mechanisms for loading datasets directly, removing the need for a docker composition intermediary.**

A collection of sample datasets for TypeDB. To start a TypeDB Core server with all sample datasets loaded, run the following commands:

1. `docker image pull vaticle/typedb-sample-data:1.0.0`
2. `docker run -p 1730:1729 vaticle/typedb-sample-data:1.0.0`

The server will be available locally on port `1730`. Please note: this is different to the default port `1729` used by TypeDB, to avoid conflicts with any pre-existing server.
