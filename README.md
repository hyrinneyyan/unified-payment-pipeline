# Unified Payment Pipeline

## Overview

This project unifies payment event pipelines across:
- Cards
- Transfers
- Bill Payments

The pipeline:
- ingests CSV files,
- transforms events to a canonical schema,
- validates records,
- outputs Parquet datasets.

---

# Setup

```bash
pip install -r requirements.txt
