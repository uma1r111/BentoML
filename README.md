# BentoML IRIS Classifier

This is a small project built to explore **[BentoML](https://docs.bentoml.org/)** and how it helps in building and serving machine learning models without relying on Flask or FastAPI directly.

The goal was to understand how BentoML simplifies packaging, serving, and containerizing ML models — and how it provides built-in API endpoints and Swagger UI for interaction.

## 🔍 Project Overview

- Dataset used: **Iris dataset**
- Model: A simple classifier trained to predict iris flower species
- Framework: **BentoML**
- Objective: Serve a model as an API using BentoML’s `Service` class

## ✅ Key Features

- **No Flask/FastAPI needed**: Uses BentoML’s native service framework
- **Interactive Swagger UI**: Automatically generated for testing input/output
- **Self-contained package**: Easily containerized via Docker
- **Easy deployment workflow**:
  - Build your model
  - Define a service
  - Package using `bentoml build`
  - Serve with `bentoml serve`

## 📦 BentoML Commands Used

### Build the project package

```bash
bentoml build
```
### Serve the model with live reloading

```bash
bentoml serve service.py:svc --reload
```

### You can containerize the built Bento using BentoML’s Docker integration
```bash
bentoml containerize iris_classifier:latest
```


