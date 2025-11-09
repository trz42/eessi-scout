# EESSI-Scout

[![CI](https://github.com/trz42/EESSI-Scout/actions/workflows/ci.yml/badge.svg)](https://github.com/trz42/EESSI-Scout/actions/workflows/ci.yml)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/trz42/EESSI-Scout/badge)](https://securityscorecards.dev/viewer/?uri=github.com/trz42/EESSI-Scout)

EESSI-Scout automates the process of identifying software packages missing
from the EESSI stack or ones that may be required to be renewed. It analyzes
dependencies, verifies license compatibility, and generates pull requests to
extend the EESSI software ecosystem — keeping your stack complete, compliant,
and up to date.

## Outline of goals

- Identify software packages that are available from a release of EasyBuild
  but not yet available in EESSI (and not in the process of being added).
- Focus on currently supported toolchains in EESSI (2022b, 2023a, 2023b, 2024a,
  2025a).
- For each missing package
  - Determine the dependencies that are missing in EESSI.
  - Determine the license of the package.
  - Determine if there is another version of the package in EESSI already.
- Skip packages that come with unknown or non-Open Source license.
- Create a sorted list of packages with the criteria
  - No version of package is included in EESSI yet.
  - Package has the largest number of dependencies. (try to avoid building
    dependencies one by one)
  - Toolchain is newest.
- Create a means (e.g., page or issue or something) to manually trigger the
  creation of pull requests to EESSI/software-layer using the current EB
  version, the correct toolchain and the correct easystack file (1st build
  vs rebuild).
