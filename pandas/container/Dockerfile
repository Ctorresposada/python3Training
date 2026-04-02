FROM public.ecr.aws/lambda/python:3.11

RUN yum install -y gcc libffi-devel python3-devel && \
    pip install --upgrade pip && \
    pip install pandas matplotlib boto3
ENV MPLCONFIGDIR=/tmp

COPY app.py ${LAMBDA_TASK_ROOT}

CMD ["app.lambda_handler"]
