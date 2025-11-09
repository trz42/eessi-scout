# SPDX-License-Identifier: GPL-2.0-only
# Copyright (C) 2025 EESSI-Scout Contributors
"""Placeholder test ensuring the EESSI-Scout package imports correctly."""

from eessi_scout import hello


def test_hello() -> None:
    assert hello() == "Hello, EESSI-Scout!"
