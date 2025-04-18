# Personal website

This is the public repo where all the code to deploy my personal website is located. This page is built entirely with the python library [reflex](https://reflex.dev/) and deployed it a vercel app. You can check it at https://osllogon.com.

## Install dependencies

To manage the dependencies this project uses [uv](https://docs.astral.sh/uv). Therefore, to install the required packages you just need to execute:

    uv sync

## Instructions to deploy

The deployment of this project is done through vercel manually, so this has two stages. The first one would be to compile and create a frontend we can then upload to vercel. For that, we have to execute the following command:

    reflex export --frontend-only --no-zip

This will create the version we need to upload inside a folder called `.web/`. Then, we can deploy it with vercel by command line. If you have not installed vercel just execute:

    npm i -g vercel

Then, to upload the website to vercel you just have to run the following:

    cd .web
    vercel --prod

All of this taking into account that a vercel account has to be created previously. 