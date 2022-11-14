FROM mcr.microsoft.com/playwright:focal

RUN apt-get update && apt-get install -y python3-pip
COPY . .
RUN pip3 install ChatstatTikTokApi
RUN python -m playwright install