# Krishna SAP Azure Analytics Pipeline

End-to-end data engineering & analytics pipeline simulating SAP FICO/SD data — implements a medallion architecture (bronze/silver/gold), MDM-style deduplication, a star schema, and SQL/Python-based analytics, designed to map onto Azure Synapse/Fabric.

## Status: Phase 1 complete — Mock SAP Data Generator

Generates realistic, relationally-consistent mock data mimicking core SAP tables:

| Table                     | SAP Reference | Description                                                                |
|---------------------------|---------------|----------------------------------------------------------------------------|
| `customer_master.csv`     | KNA1          | 1,000 customers + 3 intentional near-duplicates (for dedup practice)       |
| `vendor_master.csv`       | LFA1          | 1,000 vendors                                                              |
| `material_master.csv`     | MARA          | 200 materials with unit pricing                                            |
| `sales_order_header.csv`  | VBAK          | 1,000 sales orders                                                         |
| `sales_order_line.csv`    | VBAP          | Line items (1–5 per order), amount derived from quantity × material price  |
| `finance_header.csv`      | BKPF          | 1,000 finance postings, includes a few intentionally backdated documents   |
| `finance_line.csv`        | BSEG          | Debit/credit line items per posting                                        |

**Design choices:**
- Header/item table splits mirror real SAP structure (one order → many line items)
- Foreign keys are genuine and consistent (e.g., every `material_id` in line items exists in `material_master`, and `amount` is correctly derived from a real price lookup)
- Intentional data-quality issues (near-duplicate customers, backdated postings) are injected on purpose, to give later pipeline phases real problems to solve

## Tech Stack
- **Python** — pandas, Faker
- **SQLite** (upcoming, Phase 2+) — local warehouse layer
- **matplotlib** (upcoming, Phase 6) — visualization
- Designed to map onto **Azure Synapse / Microsoft Fabric** for a cloud deployment path

## Roadmap
- [x] Phase 1 — Mock SAP data generation
- [ ] Phase 2 — Bronze layer (raw ingestion, full + incremental load)
- [ ] Phase 3 — Silver layer (cleaning, MDM-style deduplication)
- [ ] Phase 4 — Gold layer (star schema)
- [ ] Phase 5 — SQL analytics (YoY trends, vendor spend, AP aging)
- [ ] Phase 6 — Visualization (matplotlib)
- [ ] Phase 7 — Orchestration (optional)

## How to run
pip install pandas faker matplotlib
python generate_mock_data.py

Outputs land in `data/raw/`.