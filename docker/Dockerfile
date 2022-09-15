# Install python
FROM python:3.10

# Install sudo
RUN apt-get update && \
    apt-get -y install sudo

# Add User
ARG USERNAME=user

RUN useradd -m -d /home/${USERNAME} ${USERNAME} && \
    chown -R ${USERNAME} /home/${USERNAME} && \
    adduser ${USERNAME} sudo && \
    echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

ENV PATH="/home/${USERNAME}/.local/bin:${PATH}"

USER user

# Workspace
ENV WORKSPACE=/project
WORKDIR ${WORKSPACE}

# Copy and install
COPY --chown=user:user ./requirements.txt ${WORKSPACE}/requirements.txt

RUN pip install --no-cache-dir --upgrade -r ${WORKSPACE}/requirements.txt

COPY --chown=user:user ./ ${WORKSPACE}/

RUN python -m spacy download en_core_web_sm
RUN cd ${WORKSPACE}


COPY ./data /project/data
COPY ./experiments /project/experiments
COPY ./wordnet /project/wordnet
CMD ["jupyter-lab","--ip=0.0.0.0","--no-browser"]
