# Changelog

All notable changes to this project will be documented in this file.

## [0.1.0] - 2026-05-08

### Added
- **Core Engine**: Implemented a job scheduler for handling multi-threaded clone and build operations.
- **Build System**: Added support for project building, including a specialized KiCad compiler.
- **Packaging**: Integrated build packaging and persistence with ZIP file generation.
- **Web Interface**: Developed a basic Flask-based web server with project management (CRD operations), build status monitoring, and build downloads.
- **Persistency**: Added database models and persistence for projects and logs.
- **Infrastructure**: Added Docker and Docker Compose support, and an environment generation script.
- **Logging**: Integrated a custom logging system with support for persistency.


---
*Initial release of Benkins - A simple CI/CD tool.*
