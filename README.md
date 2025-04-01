# e-Commerce Store

To run the backend, use:

```bash

cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

PYTHONPAT=. python src/app.py
```

The SwaggerUI will be available at [http://localhost:8000/docs](http://localhost:8000/docs) once the backend is started

To run the unit test, use:

```bash
cd backend
source venv/bin./activate
pip install -r test-requirements -r requirements.txt
PYTHONPATH=. python -m pytest tests/unit_tests/
```
