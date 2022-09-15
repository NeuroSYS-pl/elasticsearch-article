# FROM continuumio/miniconda3:4.10.3p1
FROM jupyter/base-notebook:latest

ENV WORKSPACE=/project
WORKDIR ${WORKSPACE}

RUN conda install \
    numpy \
    pandas \
    matplotlib \
    jupyterlab

RUN pip install \
    elasticsearch==7.17.3 \
    spacy==3.3.0 \
    ipywidgets

RUN python -m spacy download en_core_web_sm

COPY ./data /project/data
COPY ./experiments /project/experiments
COPY ./wordnet /project/wordnet
CMD ["jupyter-lab","--ip=0.0.0.0","--no-browser","--allow-root"]