## Hurb Challenge - Machine Learning

In this project, we explore the [hotel booking demand dataset](https://www.sciencedirect.com/science/article/pii/S2352340918315191) to build a model which can predict whether a customer is prone to cancel a booking.

With such a model, we can develop strategies to approach the customers and ensure they will not cancel a booking, so increasing the revenue.

You can find out all the steps from reading data to training model in  `notebooks` dir. They are enumerated in straightforward order, easy to follow. You can follow it using Github GUI, or you can clone this repository and use your own [Jupyter](https://jupyter.org/). There is presented a `requirements.txt` file, which contains all needed libraries to open and run these notebooks. You can install it typing `pip install -r requirements.txt` on your terminal, but it is recommended to create a [Python venv](https://docs.python.org/pt-br/3/library/venv.html) before that.

The model was trained using [Tensorflow](https://www.tensorflow.org/?hl=pt-br), a powerful library to build Deep Learning models. And it was deployed using [FastAPI](https://fastapi.tiangolo.com/), a high-performance Python framework for asynchronous backend.

You can test the model API by yourself, building the backend image locally. For that, you must have installed [Docker](https://www.docker.com/). Once you have it, you can type `docker compose up --build` on your terminal (ensure that it is opened on the root project dir) to run the backend (with the model). To make a request, you can follow the code presented in `notebooks/#05 - Predict test data using model API.ipynb`. Also, if you don't have Docker installed on your machine, you can replace the URL `http://localhost:8008/predict/v1` with `http://hurb.henchaves.com/predict/v1`, so you can access the cloud-based model deployed by my own.

