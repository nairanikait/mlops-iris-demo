
from pycaret.classification import setup, compare_models, finalize_model, save_model
from pycaret.datasets import get_data

iris = get_data('iris')

setup(
    data=iris,
    target='species',
    session_id=42,
    html=False,
    verbose=False
)

model = compare_models()
final = finalize_model(model)
save_model(final, 'iris_model')

print("Model retrained and saved successfully.")
