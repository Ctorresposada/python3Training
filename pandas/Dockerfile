FROM public.ecr.aws/lambda/python:3.11

# Install necessary packages
RUN yum install -y gcc libffi-devel python3-devel && \
    pip install --upgrade pip && \
    pip install pandas matplotlib boto3

# Copy function code
COPY app.py ${LAMBDA_TASK_ROOT}

CMD ["app.lambda_handler"]
