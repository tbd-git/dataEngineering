# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A personal data-engineering learning workspace, not an application. There is no package manifest, no build, no test suite, and no entry point. The unit of work is a single numbered notebook or script at the repo root, each self-contained and re-runnable top to bottom:

| File | Topic |
| --- | --- |
| [1.pySparkLearn.ipynb](1.pySparkLearn.ipynb) | DataFrame creation, window functions (cumulative sum, `dense_rank`), messy-date parsing |
| [2.employ_dataFrame_window.ipynb](2.employ_dataFrame_window.ipynb) | Same 20-row employee dataset, `row_number` ranking ("2nd highest salary per department") |
| [3.pythonLearn.ipynb](3.pythonLearn.ipynb) | Dicts, classes, public/protected/private conventions, a boto3 S3 read |
| [4.python_listComprehenssion.ipynb](4.python_listComprehenssion.ipynb) | List comprehension exercises |
| [5.sparkOptimization.md](5.sparkOptimization.md) | Prose reference: partitioning, broadcast joins, caching, narrow vs. wide transformations, `spark-submit` tuning |
| [6.sqlLearn.sql](6.sqlLearn.sql) | Empty placeholder |
| [testAWS.py](testAWS.py) | Reads `test_aws_omm.csv` from S3 via boto3; ends mid-edit at an unfinished `upsertEntries` stub |
| [Steps.txt](Steps.txt) | The original setup notes (see caveat below) |

Notebooks 1 and 2 duplicate the same employee dataset and date-cleaning cell on purpose — each notebook stands alone rather than importing shared code. Keep that convention; don't factor the fixtures into a shared module unless asked.

## Environment

The committed-in-place virtualenv is `dataEngEnv/` (excluded from git by its own `dataEngEnv/.gitignore`, which ignores `*`). There is no root `.gitignore`.

- Python 3.13.7, PySpark 4.1.2, boto3, JupyterLab 4.6, pandas 3.0, numpy 2.5, plus `ipython-sql`, `duckdb`, `databricks-sql-connector`, and `psycopg2-binary` from SQL experiments
- **`pyarrow` is deliberately absent.** PySpark's `sql` extra wants it, so anything Arrow-backed — `toPandas()`, `spark.createDataFrame(pandas_df)`, pandas UDFs, `spark.sql.execution.arrow.pyspark.enabled` — will fail. Pure Spark DataFrame work is unaffected.
- Spark needs a JDK; Temurin 17 is installed and `JAVA_HOME` is already set machine-wide. `HADOOP_HOME` is unset (fine for local `local[*]` runs, but `winutils` is absent so anything needing native Hadoop IO on Windows will fail)

```powershell
dataEngEnv\Scripts\Activate.ps1      # PowerShell — resolves its own path, works
dataEngEnv\Scripts\jupyter.exe lab   # or run notebooks through the VS Code kernel
dataEngEnv\Scripts\python.exe testAWS.py
```

Gotchas worth knowing before you debug something for the wrong reason:

- **Do not `source dataEngEnv/Scripts/activate` from Bash.** That script hardcodes the venv's original creation path (`C:\Users\nsdeo\OneDrive\Documents\gitTest\dataEngineering\dataEngEnv`), which no longer exists. Invoke `dataEngEnv/Scripts/python.exe` directly instead, or use `Activate.ps1`.
- `Steps.txt` says to `pip install findspark` and call `findspark.init()`. **findspark is not installed and is not used** — PySpark is a normal venv package here, so `from pyspark.sql import SparkSession` works unaided. Treat that file as history.
- Notebook 2's first cell is `%load_ext sql`, which needs `ipython-sql` — that *is* installed (0.5.0), so the cell succeeds. Nothing in the notebook actually uses `%sql` afterwards; every later cell is plain PySpark.

## Clean-machine setup (to run `1.pySparkLearn.ipynb`)

The notebook needs only PySpark and a Jupyter kernel — no pandas, no numpy, no pyarrow, no findspark, no local Spark install. Verified by executing its primitives (`createDataFrame`, `Window` + `F.sum`, `F.dense_rank`, `F.coalesce`/`F.try_to_date`) against exactly this stack.

**1. Java 17 or newer.** Spark 4 dropped Java 8/11 — those fail outright. Install a JDK (Temurin 17 is what this repo is verified on) and set `JAVA_HOME` to the JDK root:

```powershell
winget install EclipseAdoptium.Temurin.17.JDK
# new shell, then confirm:
java -version          # expect 17.x or newer
echo $env:JAVA_HOME    # must be set, and must be the JDK root, not \bin
```

**2. Python 3.10+.** PySpark 4.1.2 declares `Requires-Python >=3.10`; this repo uses 3.13.7.

**3. Venv and packages.**

```powershell
py -3.13 -m venv dataEngEnv
dataEngEnv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install pyspark==4.1.2 ipykernel
```

`pyspark` bundles the Spark JARs and pulls in `py4j` — that is the whole runtime. Add `ipykernel` only so VS Code / Jupyter can attach a kernel; swap it for `jupyterlab` if you want the browser UI (`jupyter lab`). To reproduce the full committed environment instead of the minimum, add `boto3 jupyterlab pandas numpy ipython-sql`.

**4. Select the interpreter** `dataEngEnv\Scripts\python.exe` as the notebook kernel, then run all cells.

Expected noise on a healthy Windows run — all harmless, do not chase them:

- `WARN NativeCodeLoader: Unable to load native-hadoop library` (no `winutils`; in-memory work is fine)
- `WARN Utils: Service 'SparkUI' could not bind on port 4040` (another Spark session holds it; it retries 4041)
- `WARN WindowExec: No Partition Defined for Window operation!` — genuine and expected for the cumulative-salary cell, which uses `Window.orderBy("ID")` with no `partitionBy`

Cell 3 of the notebook ends in a committed `AttributeError: 'NoneType' object has no attribute 'filter'`. That is a real bug in the saved code, not a setup problem — see below.

## Working in the notebooks

- **Notebooks are committed with their outputs**, including tracebacks from cells that were left broken mid-experiment (e.g. [1.pySparkLearn.ipynb](1.pySparkLearn.ipynb) chains `.filter()` onto the result of `.show()`, which returns `None`). Stored output is a snapshot of the last run, not a statement of intent — when fixing a cell, re-run it so the saved output matches the code.
- Because outputs are tracked, diffs on these files are large and noisy. Expect that; don't strip outputs repo-wide as a drive-by cleanup.
- Style across the notebooks is `import pyspark.sql.functions as F`, `camelCase` locals, and `df`/`dfEmp`/`df_cleaned`-style names. It's inconsistent already — match the surrounding cell rather than the repo.

## AWS

`testAWS.py` and the notebook 3 S3 cell use the default boto3 credential chain, reading `AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY` / `AWS_DEFAULT_REGION` from the ambient environment. There is no `.env` and no credentials file in the repo; expect `NoCredentialsError` or `AccessDenied` unless the shell is already configured. Fixed targets in the code: bucket `aws-learning-omm`, key `test_aws_omm.csv` (a copy of which is at the repo root for offline use), region `ap-south-1`.

`AWS_materials/` is extracted third-party workshop content (boto3/DynamoDB/S3/STS notebook, DynamoDB CLI param JSONs, VPC/IAM/EC2 and ECS/Lambda PDFs), committed alongside the original `.zip`s and macOS `__MACOSX` resource forks. It is reference material — not code this repo runs.

`BronzeData/`, `SilverData/`, `GoldData/`, `performance-optimization/`, and `terraform_demo/` are empty, untracked placeholders for planned medallion-architecture and Terraform work.

## Git

The remote uses a promotion flow: `feature-dev-*` → `development` → `sit` → `uat` → `main`, with merges landing on `main` via pull request. The current branch is `feature-dev-new-file`. Branch before committing if you find yourself on `main`.
