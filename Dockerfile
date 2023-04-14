FROM python:3.11.0-alpine

ENV SECRET_KEY='9xdnakz--ip!3d(qzwpcq$#62r5!c47#f*ti9^=dc^x40)#\$ww'

WORKDIR /app

COPY req.txt /app/

RUN apk update &&  apk add postgresql-dev gcc python3-dev musl-dev \
    py3-setuptools tiff-dev jpeg-dev openjpeg-dev zlib-dev \
    freetype-dev lcms2-dev libwebp-dev tcl-dev tk-dev harfbuzz-dev \
    fribidi-dev libimagequant-dev libxcb-dev libpng-dev
RUN pip install --upgrade pip

RUN pip install -r req.txt

COPY . /app

EXPOSE 2284